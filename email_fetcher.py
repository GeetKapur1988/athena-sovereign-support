import imaplib
import email
from email.header import decode_header

def fetch_unread_emails(email_user, email_pass, imap_server="imap.hostinger.com"):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_user, email_pass)
        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()

        emails = []

        for num in email_ids:
            status, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")
                    from_ = msg.get("From")
                    emails.append({"from": from_, "subject": subject})
        return emails
    except Exception as e:
        print(f"Failed to fetch emails: {e}")
        return []
