import boto3
import sys
from botocore.exceptions import ClientError
from pprint import pprint

profile=sys.argv[1]

session = boto3.Session(profile_name=profile)   
client = session.client('s3')

list_bucket_response = client.list_buckets()


for bucketname in list_bucket_response['Buckets']:
    try:
        bucket_encryption_response = client.get_bucket_encryption(Bucket=bucketname['Name'])
        print(bucketname['Name'] + ', ' + str(bucket_encryption_response['ServerSideEncryptionConfiguration']['Rules']))
    except ClientError as err:
        #print(err)
        print(bucketname['Name'] + ' ,'+ 'Encryption Not Found')
