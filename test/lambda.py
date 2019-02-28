import boto3
import botocore
import json
import os
from emailgen import Emailgen

# s3 = boto3.resource('s3', region_name = 'us-east-1')

# bucket_name = 'inbox-bucket-test'
# bucket_name1 = 'inbox-bucket-testresized'

# bucket = s3.Bucket(bucket_name)
# print("created source bucket\n")

# bucket1 = s3.Bucket(bucket_name1)
# print("created destination bucket\n")

# def upload(filename):
#   fileToBeUploaded = os.getcwd()+'/eml/'+filename
#   key = filename
#   bucket.upload_file(fileToBeUploaded, key)

# for object in bucket1.objects.all():
#   x = []
#   x.append(object)
#   print(object)


def test1():
  emailBlob = Emailgen('sanjeevsiva17', 'hellloworld', 'adasd', 'nil', 'nil', 'emailgen.py', 'lambda.py')
  # assertAttachment(fromAddress, files)

test1()