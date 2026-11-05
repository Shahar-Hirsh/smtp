import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


receiver_email = "merrygeva312@gmail.com"
sender_email = input("enter the email you want to send from - ")
password = input("enter the password - ")

msg = MIMEMultipart()

msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "שליחת SMTP עם קובץ - שחר הירש"

email_text = """ שחר הירש
"""

msg.attach(MIMEText(email_text, "plain"))

if os.path.exists('joke.txt'):
    with open('joke.txt', "rb") as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())

    encoders.encode_base64(part)

    part.add_header("Content-Disposition",f"attachment; filename=joke.txt")

    msg.attach(part)


    try:
        server = smtplib.SMTP("smtp.gmail.com", 25)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"error {e}")

    else:
        print("Email sent successfully!")
        server.quit()

else:
    print("error file not found")
