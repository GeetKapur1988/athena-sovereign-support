from fastapi import FastAPI
from pydantic import BaseModel
from email_fetcher import fetch_unread_emails
from mailer import send_email
import os

app = FastAPI()

EMAIL_USER = os.getenv("EMAIL_USER") or "your@domain.com"
EMAIL_PASS = os.getenv("EMAIL_PASS") or "yourpassword"

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.get("/")
def read_root():
    return {"message": "Athena Sovereign Tool API is running."}

@app.get("/fetch-emails/")
def get_emails():
    emails = fetch_unread_emails(EMAIL_USER, EMAIL_PASS)
    return {"unread_emails": emails}

@app.post("/send-email/")
def post_email(request: EmailRequest):
    success = send_email(
        to_email=request.to,
        subject=request.subject,
        body=request.body,
        from_email=EMAIL_USER,
        from_password=EMAIL_PASS
    )
    return {"status": "sent" if success else "failed"}
