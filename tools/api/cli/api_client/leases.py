from datetime import datetime, timedelta

import requests

def list_leases(url, auth):
    r = requests.get(url=f"{url}/leases", auth=auth, timeout=5)
    r.raise_for_status()

    return r.json()

def create_lease(url, auth):
    four_hours_from_now = datetime.now() + timedelta(hours=9)

    body = {
        "principalId": "alex@cheste.rs",
        "budgetAmount": 10,
        "budgetCurrency": "USD",
        "budgetNotificationEmails": ["alex@cheste.rs"],
        "expiresOn": four_hours_from_now.timestamp()
    }

    r = requests.post(
        f"{url}/leades",
        auth=auth,
        timeout=5,
        json=body
    )
    r.raise_for_status()

    return r.json()

def delete_lease(url, auth, account_id):
    body = {
        "principalId": "alex@cheste.rs",
        "accountId": account_id
    }

    r = requests.delete(
        f"{url}/leases",
        auth=auth,
        timeout=5,
        json=body
    )
    r.raise_for_status()

    return r.status_code
