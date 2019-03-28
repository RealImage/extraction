import boto3
import botocore
import json
import os
from emailgen import GenerateEmailBlob
import collections
import uuid 
import time

s3 = boto3.resource('s3', region_name = 'us-east-1')

source_bucket = 'qubewire-staging-email-blobs'
destination_bucket = 'qw-inbox-dev-email-attachments-bucket'

source_bucket_object = s3.Bucket(source_bucket)
destination_bucket_object = s3.Bucket(destination_bucket)

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)    

def upload(filename, emailblob):
  fileToBeUploaded = os.getcwd()+ '/' + emailblob
  key = filename
  source_bucket_object.upload_file(fileToBeUploaded, key)

def assertAttachment(fromadd, *attachments):
    bucketAttachment = []
    for key in destination_bucket_object.objects.filter(Prefix=fromadd): 
      obj = s3.Object(destination_bucket, key.key)
      string = obj.get()['Body'].read().decode('utf-8') 
      bucketAttachment.append(string)

    localAttachment=[]
    for attachment in attachments:
      with open(attachment, 'r') as myfile:
        data=myfile.read()
        localAttachment.append(data)

    result = compare(localAttachment,bucketAttachment)   
    
    if(len(bucketAttachment)==0):
      print("No attachments in mail")
      exit()
    if(result == True):
      print("Succesfully extracted ataachments")
    else:
      print("Unsucessfull, Check cloudview logs for more details!")

def CreateAndUploadEmailBlob(to, Sub, cc, bcc, *attchments):
  fromadd = str(uuid.uuid4()) + '@gmail.com'
  print(fromadd)
  emailBlob = GenerateEmailBlob(fromadd, to, Sub, cc, bcc, *attchments)
  upload(fromadd, emailBlob)
  return fromadd
 

def UploadWithnAttachments():
  attachments = ['test.json', 'test.py']
  fromadd = CreateAndUploadEmailBlob('To@gmail.com', 'Subject', 'cc@yoahoomail.com', 'bcc@ymailcom', *attachments)
  time.sleep(5)
  assertAttachment(fromadd, *attachments)

def UploadWithNoAttachments():
  attachments = []
  fromadd = CreateAndUploadEmailBlob('To@gmail.com', 'Subject', 'cc@yoahoomail.com', 'bcc@ymailcom', *attachments)
  time.sleep(5)
  assertAttachment(fromadd, *attachments)
  
UploadWithnAttachments()
UploadWithNoAttachments()