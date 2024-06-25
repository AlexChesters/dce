import sys

import inquirer

from cli.api_client.accounts import list_accounts, add_account, delete_account
from cli.actions import Action

class AccountsAction(Action):
    def list_accounts(self):
        return list_accounts(self.url, self.auth)

    def add_account(self):
        answers = inquirer.prompt([inquirer.Text("account_id", message="What is the account ID?")])
        account_id = str(answers["account_id"])

        return add_account(self.url, self.auth, account_id)

    def delete_account(self):
        accounts = self.list_accounts()

        if not accounts:
            print("[ERROR] - no accounts are currently in the pool")
            sys.exit(1)

        accounts = [account["id"] for account in accounts]

        answers = inquirer.prompt([
            inquirer.List(
                "account_id",
                message="Select the account ID to be removed from the pool",
                choices=accounts
            )
        ])
        account_id = str(answers["account_id"])

        return delete_account(self.url, self.auth, account_id)
