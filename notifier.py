import smtplib
from email.mime.text import MIMEText
import sys
sys.stdout.reconfigure(encoding='utf-8')

EMAIL_ADDRESS = "ayushchatterjee2005dak35@gmail.com"
EMAIL_PASSWORD = "ncds quyw ygpf zvrz"  # App password, not your main password

def send_email_notification(to_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
