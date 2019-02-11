import boto3
import botocore
import json
import os

s3 = boto3.resource('s3', region_name = 'us-east-1')

bucket_name = 'inbox-bucket-test'
bucket_name1 = 'inbox-bucket-testresized'

bucket = s3.Bucket(bucket_name)
print("created source bucket\n")

bucket1 = s3.Bucket(bucket_name1)
print("created destination bucket\n")

fileToBeUploaded = os.getcwd()+'/eml/email_sample.eml'
key = 'email_sample'
bucket.upload_file(fileToBeUploaded, key)

for object in bucket1.objects.all():
  print(object)
    