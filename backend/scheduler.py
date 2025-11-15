from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import requests
import logging
import pytz
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")


def send_daily_horoscopes():
    if not ADMIN_API_KEY:
        logger.error(
            "ADMIN_API_KEY is not set – skipping daily horoscope job for safety."
        )
        return

    try:
        logger.info(f"Starting daily horoscope send at {datetime.now()}")

        headers = {"X-Admin-Token": ADMIN_API_KEY}
        response = requests.post(
            "http://localhost:6100/api/send-all-horoscopes",
            headers=headers,
            timeout=60,
        )

        if response.status_code == 200:
            try:
                result = response.json()
                logger.info(
                    f"Daily horoscopes sent successfully: {result.get('message')}"
                )
            except Exception:
                logger.info("Daily horoscopes sent successfully (no JSON body).")
        else:
            logger.error(
                f"Failed to send horoscopes: {response.status_code} {response.text}"
            )
    except Exception as e:
        logger.error(f"Error in daily horoscope send: {str(e)}")


def start_scheduler():
    budapest_tz = pytz.timezone("Europe/Budapest")

    scheduler = BackgroundScheduler(timezone=budapest_tz)

    scheduler.add_job(
        send_daily_horoscopes,
        CronTrigger(hour=8, minute=0, timezone=budapest_tz),
        id="daily_horoscope",
        name="Send daily horoscopes at 08:00 Budapest time",
        replace_existing=True,
    )

    scheduler.start()
    logger.info(
        "Scheduler started - Daily horoscopes will be sent at 8:00 AM Europe/Budapest time"
    )
    logger.info(f"Current container time: {datetime.now()}")
    logger.info(f"Current Budapest time: {datetime.now(budapest_tz)}")

    return scheduler
