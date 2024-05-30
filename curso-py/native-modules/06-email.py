# Since 2024, Google no longer allows acsses to your acount from third parties >:(

# Multipurpose Internet Mail Extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

path = Path("native-modules/jelly.jpg")
mime_image = MIMEImage(path.read_bytes())
message = MIMEMultipart()
message["from"] = "Murphy"
message["to"] = "clmonsevl@gmail.com"
message["subject"] = "This is a test"
body = MIMEText("Body of the message")
message.attach(body)
message.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # To indentify ourselves with the SMTP name and the domain that we will use to send the email
    smtp.starttls()  # So that the message is encrypted Transport Layer Security

    smtp.login("clmonsevl@gmail.com", "imsherlocked1412")
    smtp.send_message(message)
    print("Message sent")
