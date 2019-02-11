import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import datetime
import re 

html_data = """
        <html>
            <head></head>
            <body>
                <p> hello world </p>
            </body>
        </html>
        """

msg = MIMEMultipart('alternative')
msg['Subject'] = raw_input('Subject: ')

From = raw_input('From: ')
msg['From'] = '"hello world!," <'+ From +'>'
# +re.findall(r"^[^@]+", From)+
msg['To'] = raw_input('To: ')
msg['Cc'] = raw_input('Cc: ')
msg['Bcc'] = raw_input('Bcc: ')
msg['Date'] = str(datetime.datetime.now())
part = MIMEText(html_data, 'html')
msg.attach(part)



part = MIMEBase('application', "octet-stream")
part.set_payload(open("test.json", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="test.json"')

msg.attach(part)

# headers = ... dict of header key / value pairs ...


# for key in headers:
#     value = headers[key]
#     if value and not isinstance(value, basestring):
#         value = str(value)
#     msg[key] = value


outfile_name = ("eml/email_sample.eml")
with open(outfile_name, 'w') as outfile:
    gen = generator.Generator(outfile)
    gen.flatten(msg)

print ("=========== DONE ============")