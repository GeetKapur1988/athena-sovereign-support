import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load from environment
EMAIL_HOST = os.getenv("EMAIL_HOST")  # Example: smtp.hostinger.com
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "465"))  # SSL Port
EMAIL_ADDRESS = os.getenv("EMAIL_USER")  # support@entranceadda.com
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # G@xxxx format

def send_email(to_address, subject, content):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject

        # You can style this if needed
        msg.attach(MIMEText(content, 'plain'))

        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"✅ Email sent to {to_address}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_address}: {e}")
