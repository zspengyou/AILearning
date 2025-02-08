import os

from boto3 import Session


def print_user_policy(session: Session, user_name: str):
    # Create an IAM client
    iam_client = session.client('iam')
    # List attached managed policies
    response = iam_client.list_attached_user_policies(UserName=user_name)
    # Print the attached policies
    for policy in response['AttachedPolicies']:
        print(f"Policy Name: {policy['PolicyName']}, Policy ARN: {policy['PolicyArn']}")

def upload_file(glacier):
    response = glacier.upload_archive(
        vaultName='great-memory-backup-us-east-1',
        archiveDescription='sublime backup',
        body=open('/Users/JayZhou/Downloads/jaySublime.zip', 'rb')
    )
    print(response)
    print(response['archiveId'])


def retrive_fileMetaData(glacier):
    # Step 1: Initiate inventory retrieval job
    response = glacier.initiate_job(
        vaultName='your-vault-name',
        jobParameters={'Type': 'inventory-retrieval'}
    )
    job_id = response['jobId']
    # Step 2: Poll the job status (this can take hours to complete)
    job_status = glacier.describe_job(vaultName='your-vault-name', jobId=job_id)
    if job_status['Completed']:
        # Step 3: Download the inventory once the job is completed
        output = glacier.get_job_output(vaultName='your-vault-name', jobId=job_id)
        print(output['body'].read().decode('utf-8'))

def multipart_upload(s3_client, bucket_name, file_path, object_name):
    # File size
    file_size = os.path.getsize(file_path)
    print(file_size)

    # Start multipart upload
    multipart_upload = s3_client.create_multipart_upload(
        Bucket=bucket_name,
        Key=object_name,
        StorageClass='DEEP_ARCHIVE'
    )
    print(multipart_upload)
    #    StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE'|'OUTPOSTS'|'GLACIER_IR'|'SNOW'|'EXPRESS_ONEZONE',

    upload_id = multipart_upload['UploadId']

    # Upload parts
    part_size = 50 * 1024 * 1024  # 5 MB per part (minimum)
    parts = []
    try:
        with open(file_path, 'rb') as file:
            part_number = 1
            while file.tell() < file_size:
                # Read the file part by part
                part_data = file.read(part_size)

                # Upload each part
                part_response = s3_client.upload_part(
                    Body=part_data,
                    Bucket=bucket_name,
                    Key=object_name,
                    PartNumber=part_number,
                    UploadId=upload_id
                )
                print(part_number)
                print(part_response['ETag'])
                parts.append({
                    'ETag': part_response['ETag'],
                    'PartNumber': part_number
                })

                part_number += 1

        # Complete the multipart upload
        s3_client.complete_multipart_upload(
            Bucket=bucket_name,
            Key=object_name,
            UploadId=upload_id,
            MultipartUpload={'Parts': parts}
        )
        print(f"Upload complete for {object_name}!")

    except Exception as e:
        # Abort the multipart upload in case of error
        s3_client.abort_multipart_upload(
            Bucket=bucket_name,
            Key=object_name,
            UploadId=upload_id
        )
        print(f"Error occurred: {e}, upload aborted!")