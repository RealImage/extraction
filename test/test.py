import boto3
import botocore
import json
import os
from emailgen import Emailgen
import collections

s3 = boto3.resource('s3', region_name = 'us-east-1')

bucket_name = 'inbox-bucket-test'
bucket_name1 = 'inbox-bucket-testresized'

bucket = s3.Bucket(bucket_name)
print("created source bucket\n")

bucket1 = s3.Bucket(bucket_name1)
print("created destination bucket\n")


def upload(filename):
  fileToBeUploaded = os.getcwd()+'/eml/'+filename
  key = filename
  bucket.upload_file(fileToBeUploaded, key)

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)    

def assertAttachment(From, *attachments):
    objectlist = []
    for key in bucket1.objects.filter(Prefix=From): 
      objectlist = (objectlist + key.key.split("/")[-1:])
    print(objectlist)   
    result = compare(attachments,objectlist)   
    if(result == True):
      print("Succesfully extracted ataachments")
      print(objectlist)  
    else:
      print("Unsucessfull, Check cloudview logs for more details!")

def test1(From, to, Sub, cc, bcc, *attchments):
  emailBlob = Emailgen(From, to, Sub, cc, bcc, *attchments)
  
  print("Updating bucket information")
  print("Uploading to bucket\n")
  upload(From)

  print("Checking Destination bucket\n")
  assertAttachment(From, *attachments)

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
# assertAttachment('sanjeevsiva17@gmail.com', 'test.json')
