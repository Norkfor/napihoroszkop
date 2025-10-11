from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_daily_horoscopes():
    try:
        logger.info(f"Starting daily horoscope send at {datetime.now()}")
        response = requests.post("http://localhost:6100/api/send-all-horoscopes")
        if response.status_code == 200:
            result = response.json()
            logger.info(f"Daily horoscopes sent successfully: {result['message']}")
        else:
            logger.error(f"Failed to send horoscopes: {response.status_code}")
            
    except Exception as e:
        logger.error(f"Error in daily horoscope send: {str(e)}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(
        send_daily_horoscopes,
        CronTrigger(hour=8, minute=0),
        id='daily_horoscope',
        name='Send daily horoscopes at 08:00',
        replace_existing=True
    )
    
    scheduler.start()
    logger.info("Scheduler started - Daily horoscopes will be sent at 8:00 AM")
    
    return scheduler
