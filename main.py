import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv 

# load .env file  
load_dotenv()


# email details  
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("EMAIL_AUTO_PASS")

# print(f"sender email: {sender_email} and password: {password}")




