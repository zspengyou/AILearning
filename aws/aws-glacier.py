import sys

import boto3

from aws.aws_util import print_user_policy

session = boto3.Session(profile_name='personalAccount', region_name='us-east-1')
# fix1: add region
# fix2: add permission for user


# print_user_policy(session,'jay_s3')

glacier = session.client('glacier')
print(glacier)
# glacier = boto3.client('glacier')
response = glacier.upload_archive(
    vaultName='great-memory-backup-us-east-1',
    archiveDescription='sublime backup',
    body=open('/Users/JayZhou/Downloads/jaySublime.zip', 'rb')
)
print(response)
print(response['archiveId'])
