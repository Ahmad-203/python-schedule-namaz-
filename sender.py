import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = os.environ["EMAIL_USER"]
app_password = os.environ["EMAIL_PASSWORD"]
receiver_email = os.environ["RECEIVER_EMAIL"]

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Daily Email"

body = "Hello 👋 This is automated email."
message.attach(MIMEText(body, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()

print("Email Sent Successfully")
