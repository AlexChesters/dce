from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

def get_auth(hostname):
    return BotoAWSRequestsAuth(aws_host=hostname, aws_region="eu-west-1", aws_service="execute-api")
