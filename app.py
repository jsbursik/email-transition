import os
import csv

import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

sender_email = "noreply@holidayautogroup.com"
password = os.environ.get("NOREPLY_PASS")

msg = MIMEMultipart("alternative")


with open('list.csv') as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        msg["Subject"] = f'{row["Display name"]}, sign-in to your new email.'
        msg["From"] = sender_email
        msg["To"] = row["Previous Email"]
        text = """\
            """
        html = """\
            
            """
