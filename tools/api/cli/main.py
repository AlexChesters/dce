import argparse
from urllib.parse import urlparse

import inquirer

from cli.utils.auth import get_auth
from cli.actions.accounts import AccountsAction

parser = argparse.ArgumentParser(description="interact with the DCE API")
parser.add_argument("--api-url")
args = parser.parse_args()

url = urlparse(args.api_url)

accounts_action = AccountsAction(url.geturl(), get_auth(url.hostname))

answers = inquirer.prompt([
    inquirer.List(
        "action",
        message="Which action do you want to perform?",
        choices=[
            ("List accounts", accounts_action.list_accounts),
            ("Add new account", accounts_action.add_account),
            ("Remove an account", accounts_action.delete_account)
        ]
    )
])

fn = answers["action"]
print(fn())
