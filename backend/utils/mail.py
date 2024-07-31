import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to_email, subject, message):
    try:
        sender = os.getenv('EMAIL')
        password = os.getenv('EMAIL_PASSWORD') 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        server.login(sender, password)
        email_message = MIMEMultipart()
        email_message['From'] = sender
        email_message['To'] = to_email
        email_message['Subject'] = subject

        email_message.attach(MIMEText(message, 'plain'))
        server.sendmail(sender, to_email, email_message.as_string())
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
