from datetime import datetime, timedelta
import sys

import inquirer

from cli.api_client.leases import list_leases, create_lease, delete_lease
from cli.actions import Action

class LeasesAction(Action):
    def list_leases(self):
        return list_leases(self.url, self.auth)

    def create_lease(self):
        four_hours_from_now = datetime.now() + timedelta(hours=8)
        answers = inquirer.prompt(
            inquirer.Text(
                "principal_id",
                message="Enter the name of the principal this lease is for"
            )
        )
        principal_id = answers["principal_id"]

        return create_lease(self.url, self.auth, principal_id, four_hours_from_now)

    def delete_lease(self):
        current_pairs = [
            (lease["principalId"], lease["accountId"])
            for lease in self.list_leases()
            if lease["leaseStatus"] == "Active"
        ]

        if not current_pairs:
            print("there are no current active leases")
            sys.exit(0)

        pairs_choices = [
            (f"{pair[0]} ({pair[1]})", pair)
            for pair in current_pairs
        ]

        answers = inquirer.prompt([
            inquirer.List(
                "pair",
                message="Choose the lease to be deleted",
                choices=pairs_choices
            )
        ])
        principal_id, account_id = answers["pair"]

        return delete_lease(self.url, self.auth, principal_id, account_id)
