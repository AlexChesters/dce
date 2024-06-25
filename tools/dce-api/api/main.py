import argparse
from urllib.parse import urlparse

import inquirer

from api.utils.auth import get_auth
from api.actions.accounts import list_accounts, add_account

parser = argparse.ArgumentParser(description="interact with the DCE API")
parser.add_argument("--api-url")
args = parser.parse_args()

answers = inquirer.prompt([
    inquirer.List(
        "action",
        message="Which action do you want to perform?",
        choices=[
            ("List accounts", list_accounts),
            ("Add new account", add_account)
        ]
    )
])

url = urlparse(args.api_url)

fn = answers["action"]
print(fn(url.geturl(), get_auth(url.hostname)))
