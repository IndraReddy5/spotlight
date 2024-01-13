import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.encoders import encode_base64
from email.mime.base import MIMEBase

SMTP_SERVER_HOST = "localhost"
SMTP_SERVER_PORT = "1025"
SENDER_ADDRESS = "noreply@spotlight.com"

def send_email(to, subject, msg, attachment = None):
    mail = MIMEMultipart()
    mail['From'] = SENDER_ADDRESS
    mail['Subject'] = subject
    mail['To'] = to

    mail.attach(MIMEText(msg, "html"))

    if attachment:
        with open(attachment, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(attachment)}")
            mail.attach(part)

    s = smtplib.SMTP(SMTP_SERVER_HOST, SMTP_SERVER_PORT)
    s.login(SENDER_ADDRESS, "123")
    s.send_message(mail)
    s.quit()

    if attachment:
        os.remove(attachment)

    return True