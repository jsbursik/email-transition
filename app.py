import os
import csv

import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

sender_email = "noreply@holidayautogroup.com"
password = os.environ.get("NOREPLY_PASS")

login_date = "[DATE HERE]"


text = """
    You need to view this email in HTML, if you see this contact Jordan Bursik.
"""


html = open("email.html", "r").read()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.ipower.com", 465, context=context) as server:
    print(f"Logging into {sender_email}...")
    server.login(sender_email, password)
    with open('list.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            msg = MIMEMultipart("alternative")

            msg["Subject"] = f'{row["Display name"]}, sign-in to your new email.'
            msg["From"] = sender_email
            msg["To"] = row["Previous Email"]

            msg.attach(MIMEText(text, "plain"))
            temp_HTML = html.replace("{user_name}", row["Display name"]).replace(
                "{user_email}", row["Username"]).replace("{user_pass}", row["Password"]).replace("{login_date}", login_date)
            msg.attach(MIMEText(temp_HTML, "html"))
            print(f"Sending email to {row['Display name']}...")
            server.sendmail(
                sender_email, row["Previous Email"], msg.as_string())
