from cli.api_client.accounts import list_accounts, add_account, delete_account
from cli.actions import Action

class AccountsAction(Action):
    def list_accounts(self):
        return list_accounts(self.url, self.auth)

    def add_account(self):
        return add_account(self.url, self.auth)

    def delete_account(self):
        return delete_account(self.url, self.auth)
