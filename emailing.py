import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

PASSWORD = "wzhetetgnmczbluj"
SENDER = "esending8@gmail.com"
RECEIVER = "esending8@gmail.com"

def send_email(image_path):
    # print("email sent.")
    email_message = MIMEMultipart()
    email_message["Subject"] = "New object showed up!"
    email_message["From"] = "Webcam App"
    email_message["To"] = RECEIVER
    body = "Hey, we just saw a new object."
    email_message.attach(MIMEText(body))

    part = MIMEBase('application', 'octet-stream')
    with open(image_path, "rb") as file:
        # content = file.read() #doesn't work
         part.set_payload(file.read())
        # part = MIMEApplication(file.read()) #works
    encoders.encode_base64(part)
    part["Content-Disposition"] = 'attachment; filename={}'.format(Path(image_path).name)
    email_message.attach(part)
    # email_message.attach(content, maintype="image", subtype=imghdr.what(image, content)) #doesn't work
    gmail = smtplib.SMTP("smtp.gmail.com", 587)

    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("images/71.png")
