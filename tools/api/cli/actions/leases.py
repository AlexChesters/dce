from datetime import datetime, timedelta
import sys
import uuid

import inquirer

from cli.utils.logger import Logger
from cli.api_client.leases import list_leases, create_lease, delete_lease, create_lease_auth
from cli.actions import Action

logger = Logger()

class LeasesAction(Action):
    def __get_active_leases(self):
        return [
            lease
            for lease in list_leases(self.url, self.auth)
            if lease["leaseStatus"] == "Active"
        ]

    def list_leases(self):
        leases = list_leases(self.url, self.auth)

        for lease in leases:
            principal = lease["principalId"]
            account = lease["accountId"]
            status = lease["leaseStatus"]

            logger.plain(f"{principal} - {account} ({status})")

    def create_lease(self):
        four_hours_from_now = datetime.now() + timedelta(hours=8)
        answers = inquirer.prompt([
            inquirer.Text(
                "principal_id",
                message="Enter the name of the principal this lease is for"
            )
        ])
        principal_id = answers["principal_id"]

        logger.plain(create_lease(self.url, self.auth, principal_id, four_hours_from_now))

    def delete_lease(self):
        active_leases = self.__get_active_leases()

        if not active_leases:
            print("there are no active leases")
            sys.exit(0)

        leases_choices = [
            (f"{lease["principalId"]} ({lease["accountId"]})", lease)
            for lease in active_leases
        ]

        answers = inquirer.prompt([
            inquirer.List(
                "pair",
                message="Choose the lease to be deleted",
                choices=leases_choices
            )
        ])
        principal_id, account_id = answers["pair"]

        logger.plain(delete_lease(self.url, self.auth, principal_id, account_id))

    def create_lease_auth(self):
        lease_id = uuid.uuid4()
        active_leases = self.__get_active_leases()

        if not active_leases:
            print("there are no active leases")
            sys.exit(0)

        print(active_leases)
        sys.exit(0)

        lease_data = create_lease_auth(self.url, self.auth, lease_id)
        logger.plain(lease_data)
