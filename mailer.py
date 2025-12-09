import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body, smtp_server="smtp.hostinger.com", smtp_port=587,
               from_email=None, from_password=None):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email
        msg.set_content(body)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
