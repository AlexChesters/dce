import argparse
from urllib.parse import urlparse

import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

parser = argparse.ArgumentParser()
parser.add_argument("--api-url")
args = parser.parse_args()

url = urlparse(args.api_url)

auth = BotoAWSRequestsAuth(aws_host=url.hostname, aws_region="eu-west-1", aws_service="execute-api")

r = requests.get(url=f"{url.geturl()}/accounts", auth=auth, timeout=5)
r.raise_for_status()
print(r.json())
