import argparse
from urllib.parse import urlparse

import requests

from api.utils.auth import get_auth

parser = argparse.ArgumentParser(description="interact with the DCE API")
parser.add_argument("--api-url")
args = parser.parse_args()

url = urlparse(args.api_url)

r = requests.get(url=f"{url.geturl()}/accounts", auth=get_auth(url.hostname), timeout=5)
r.raise_for_status()
print(r.json())
