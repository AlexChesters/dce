import argparse
from urllib.parse import urlparse

import inquirer

from cli.utils.auth import get_auth
from cli.actions.leases import LeasesAction
from cli.actions.accounts import AccountsAction

parser = argparse.ArgumentParser(description="interact with the DCE API")
parser.add_argument("--api-url")
args = parser.parse_args()

url = urlparse(args.api_url)

leases_action = LeasesAction(url.geturl(), get_auth(url.hostname))
accounts_action = AccountsAction(url.geturl(), get_auth(url.hostname))

section_answers = inquirer.prompt([
    inquirer.List(
        "action",
        message="Choose a section",
        choices=[("Leases", "leases"), ("Accounts", "accounts")]
    )
])


match section_answers["action"]:
    case "leases":
        answers = inquirer.prompt([
            inquirer.List(
                "action",
                message="Which action do you want to perform?",
                choices=[
                    ("List leases", leases_action.list_leases),
                    ("Create a lease", leases_action.create_lease),
                    ("Delete a lease", leases_action.delete_lease),
                    ("Create a lease authentication", leases_action.create_lease_auth)
                ]
            )
        ])
        fn = answers["action"]
        print(fn())
    case "accounts":
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
