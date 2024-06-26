from cli.api_client.leases import list_leases
from cli.actions import Action

class LeasesAction(Action):
    def list_leases(self):
        return list_leases(self.url, self.auth)
