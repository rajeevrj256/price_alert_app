import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_email(to_email, subject, message):
    try:
        sender = "so.rajeev5918@gmail.com"
        password = os.getenv('EMAIL_PASSWORD')  # Use environment variable for password

        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        server.login(sender, password)

        # Create the email
        email_message = MIMEMultipart()
        email_message['From'] = sender
        email_message['To'] = to_email
        email_message['Subject'] = subject

        email_message.attach(MIMEText(message, 'plain'))

        # Send the email
        server.sendmail(sender, to_email, email_message.as_string())
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
