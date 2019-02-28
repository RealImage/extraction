import boto3
import botocore
import json
import os
from emailgen import Emailgen

s3 = boto3.resource('s3', region_name = 'us-east-1')

bucket_name = 'email_blob_bucket'
bucket_name1 = 'email_attachment_bucket'

bucket = s3.Bucket(bucket_name)
print("created source bucket\n")

bucket1 = s3.Bucket(bucket_name1)
print("created destination bucket\n")


def upload(filename):
  fileToBeUploaded = os.getcwd()+'/eml/'+filename
  key = filename
  bucket.upload_file(fileToBeUploaded, key)

def assertAttachment(fromaddr, *files):
  for object in bucket1.objects.all():
    x = []
    x.append(object)
    print(object)

def test1(From, to, Sub, cc, bcc, *attchments):
  emailBlob = Emailgen(From, to, Sub, cc, bcc, *attchments)
  
  print("Updating bucket information")
  print("Uploading to bucket\n")
  upload("email_sample.eml")

  print("Checking Destination bucket\n")
  assertAttachment('sanjeevsiva17', 'emailgen.py', 'lambda.py')

From = raw_input("From : ")
To = raw_input("To : ")
Sub = raw_input("Subject : ")
cc = raw_input("Cc : ")
bcc = raw_input("Bcc : ")

number_of_attachments = int(raw_input("Enter the number of attachments: "))
attachments = []
for i in range(number_of_attachments):
  attachments.append(raw_input("Enter name of attachment: "))

test1(From, To, Sub, cc, bcc, *attachments)