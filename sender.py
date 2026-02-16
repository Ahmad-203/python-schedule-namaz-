import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender email and app password
sender_email = "programp306@gmail.com"
app_password = "simb xtes mftt fddh"

# Receiver email
receiver_email = "m3340898@gmail.com"

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

body = "Hello 👋\n\nThis email is sent using Python.\n\nRegards,\nAhmad"
message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

# Send email
server.sendmail(sender_email, receiver_email, message.as_string())

print("✅ Email Sent Successfully!")

server.quit()
