import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


receiver_email = "merrygeva312@gmail.com"
sender_email = input("enter the email you want to send from - ")
password = input("enter the password - ")

msg = MIMEMultipart()

msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "שליחת SMTP מ - שחר הירש"

email_text = """ שחר הירש
איך קוראים לקרנף בקיץ? חם-נף
"""
msg.attach(MIMEText(email_text, "plain"))


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
