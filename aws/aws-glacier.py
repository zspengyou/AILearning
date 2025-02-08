import sys

import boto3
import os

from aws.aws_util import print_user_policy, upload_file, retrive_fileMetaData

session = boto3.Session(profile_name='personalAccount', region_name='us-east-1')
# fix1: add region
# fix2: add permission for user


# print_user_policy(session,'jay_s3')

glacier = session.client('glacier')


s3_client = session.client('s3')

def multipart_upload(bucket_name, file_path, object_name):
    # File size
    file_size = os.path.getsize(file_path)
    print(file_size)


    upload_id = "TjWXsorg6hj5oG01f3KPXwavf.yX.7rXY0DO2zbqISCeZDLlrpGuS7vvlIc4VeeVVw06Zh8XqH7JFLkcxvg8NXmxsRqU44rda8OMoIgCN2.UuQ7koOXItVTmehBka3kF"
    # Upload parts
    part_size = 5 * 1024 * 1024  # 5 MB per part (minimum)
    parts = []
    sum = 0;
    try:
        with open(file_path, 'rb') as file:
            part_number = 1
            while file.tell() < file_size:
                # Read the file part by part
                part_data = file.read(part_size)

                # Upload each part
                print(len(list(part_data)))
                sum += len(list(part_data))

                
                part_number += 1

        # Complete the multipart upload

        print(f"Upload complete for {object_name}! + {part_number}")
        print(f"Upload complete for {object_name}! + {sum/1024/1024}")

    except Exception as e:
        # Abort the multipart upload in case of error

        print(f"Error occurred: {e}, upload aborted!")



#################################################################


# upload_idoad_file(glacier)
# retrive_fileMetaData(glacier)



multipart_upload(
    bucket_name= 'jay-intelligent-tier-for-backup',
    file_path='/Users/JayZhou/Downloads/jaySublime.zip',
    object_name = 'jaySublime.zip',
)
