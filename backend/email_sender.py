import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to_email, zodiac_sign, horoscope_html):
    smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    smtp_port_str = os.getenv('SMTP_PORT', '587')
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    
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
    
    msg = MIMEText(horoscope_html, 'html', 'utf-8')
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = f'Napi horoszkópod - {zodiac_sign}'
    
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
