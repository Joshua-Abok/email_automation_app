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

# create the email body 
message = EmailMessage()
message['subject'] = "email automation test"
message['From'] = sender_email
message['To'] = receiver_email
message.set_content(
    "Good morning, \n\n This is a email automation test using python \n\n regards, [name]"
)


# making connection for sending email  
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: 
    server.login(sender_email, password)
    server.send_message(message)
print(f"Email sent successfully to {receiver_email}")

