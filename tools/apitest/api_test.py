import argparse
from urllib.parse import urlparse

import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
import boto3

def assume_role(session, role_arn):
    client = session.client("sts")

    response = client.assume_role(
        RoleArn=role_arn,
        RoleSessionName="api-test"
    )

    return response["Credentials"]

parser = argparse.ArgumentParser()
parser.add_argument("--api-url")
args = parser.parse_args()

credentials = assume_role(
    boto3.Session(profile_name="dce-master"),
    "arn:aws:iam::637423502760:role/dce-api-admin-role"
)

url = urlparse(args.api_url)

auth = BotoAWSRequestsAuth(aws_host=url.hostname, aws_region="eu-west-1", aws_service="execute-api")

r = requests.get(url=f"{url.geturl()}/accounts", auth=auth, timeout=5)
r.raise_for_status()
print(r.json())
