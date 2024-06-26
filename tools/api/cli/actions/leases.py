from datetime import datetime, timedelta

import inquirer

from cli.api_client.leases import list_leases, create_lease, delete_lease
from cli.actions import Action

class LeasesAction(Action):
    def list_leases(self):
        return list_leases(self.url, self.auth)

    def create_lease(self):
        four_hours_from_now = datetime.now() + timedelta(hours=8)

        return create_lease(self.url, self.auth, "quickstartuser", four_hours_from_now)

    def delete_lease(self):
        answers = inquirer.prompt([
            inquirer.Text(
                "account_id",
                message="Enter the account ID"
            )
        ])
        account_id = str(answers["account_id"])

        return delete_lease(self.url, self.auth, "string", account_id)
