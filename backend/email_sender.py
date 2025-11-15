import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to_email, zodiac_sign, horoscope_html, unsubscribe_token=None):
    smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    smtp_port_str = os.getenv('SMTP_PORT', '587')
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    public_base_url = os.getenv('PUBLIC_BASE_URL', '').strip()
    frontend_base_url = os.getenv('FRONTEND_BASE_URL', '').strip()

    try:
        if smtp_port_str:
            smtp_port = int(smtp_port_str.strip())
        else:
            smtp_port = 587
    except (ValueError, AttributeError):
        smtp_port = 587

    if not smtp_user:
        raise ValueError("SMTP_USER not set!")
    if not smtp_password:
        raise ValueError("SMTP_PASSWORD not set!")

    unsubscribe_url = None
    frontend_unsubscribe_url = None

    if unsubscribe_token and public_base_url:
        base = public_base_url.rstrip('/')
        unsubscribe_url = f"{base}/api/unsubscribe?token={unsubscribe_token}"

    if unsubscribe_token and frontend_base_url:
        fbase = frontend_base_url.rstrip('/')
        frontend_unsubscribe_url = f"{fbase}/app?unsubscribeToken={unsubscribe_token}"

        footer_html = f"""
        <div style="margin-top: 30px; padding-top: 15px; border-top: 1px solid #e5e7eb; text-align: center; font-size: 12px; color: #6b7280;">
            <p style="margin: 0 0 8px 0;">
                Ezt az üzenetet a(z) <strong>{to_email}</strong> címre küldtük.
            </p>
            <p style="margin: 0;">
                Ha nem szeretnél több napi horoszkópot kapni,
                <a href="{frontend_unsubscribe_url}" style="color: #2563eb; text-decoration: underline;">
                    kattints ide a leiratkozáshoz
                </a>.
            </p>
        </div>
        """

        if "</body>" in horoscope_html:
            horoscope_html = horoscope_html.replace("</body>", footer_html + "</body>")
        else:
            horoscope_html = horoscope_html + footer_html

    msg = MIMEText(horoscope_html, 'html', 'utf-8')
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = f'Napi horoszkópod - {zodiac_sign}'

    if unsubscribe_url:
        msg['List-Unsubscribe'] = f"<{unsubscribe_url}>"
        msg['List-Unsubscribe-Post'] = "List-Unsubscribe=One-Click"

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
