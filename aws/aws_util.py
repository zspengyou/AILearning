from boto3 import Session


def print_user_policy(session: Session, user_name: str):
    # Create an IAM client
    iam_client = session.client('iam')
    # List attached managed policies
    response = iam_client.list_attached_user_policies(UserName=user_name)
    # Print the attached policies
    for policy in response['AttachedPolicies']:
        print(f"Policy Name: {policy['PolicyName']}, Policy ARN: {policy['PolicyArn']}")