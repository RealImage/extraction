import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import datetime
import re 

def Emailgen(From, to, subject, cc, bcc, *attachments):
    html_data = """
            <html>
                <head></head>
                <body>
                    <p> hello world </p>
                </body>
            </html>
            """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject

    From = From
    msg['From'] = '"hello world!," <'+ From +'>'
    # +re.findall(r"^[^@]+", From)+
    msg['To'] = to
    msg['Cc'] = cc
    msg['Bcc'] = bcc
    msg['Date'] = str(datetime.datetime.now())
    part = MIMEText(html_data, 'html')
    msg.attach(part)


    for file in attachments:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=' + file)
        msg.attach(part)

    outfile_name = ("eml/email_sample.eml")
    with open(outfile_name, 'w') as outfile:
        gen = generator.Generator(outfile)
        gen.flatten(msg)

    print ("=========== DONE ============")