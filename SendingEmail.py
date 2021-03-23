from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587

username = "user@gmail.com"
password = "password"

from_email = username
to_list = ["to@gmail.com"]

message = MIMEMultipart("alternative")
message["subject"] = "test subject"
message["from"] = from_email

plain_txt ="""Hi

It is a test email!

"""

try:
    txt_part = MIMEText(plain_txt, "plain")
    message.attach(txt_part)
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()   
    email_conn.starttls()
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, message.as_string())
    email_conn.quit()
except:
    print("login error")
    



