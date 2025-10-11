import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to_email, zodiac_sign, horoscope_html):
    smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    
    msg = MIMEText(f"""

                   {horoscope_html}
                   
                   """,'html')
    
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = f'Napi horoszkópod - {zodiac_sign}'
    
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)