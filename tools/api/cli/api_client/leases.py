import sys
from datetime import datetime

import requests

def list_leases(url: str, auth):
    r = requests.get(url=f"{url}/leases", auth=auth, timeout=5)
    r.raise_for_status()

    return r.json()

def create_lease(url: str, auth, principal_id: str, expires: datetime):
    body = {
        "principalId": principal_id,
        "budgetAmount": 10,
        "budgetCurrency": "USD",
        "budgetNotificationEmails": ["alex@cheste.rs"],
        "expiresOn": int(expires.timestamp())
    }

    r = requests.post(
        f"{url}/leases",
        auth=auth,
        timeout=5,
        json=body
    )

    if not r.ok:
        print(f"non-200 status code received: {r.status_code}")
        print(r.json())
        sys.exit(1)

    return r.json()

def delete_lease(url: str, auth, principal_id: str, account_id: str):
    body = {
        "principalId": principal_id,
        "accountId": account_id
    }

    r = requests.delete(
        f"{url}/leases",
        auth=auth,
        timeout=5,
        json=body
    )

    if not r.ok:
        print(f"non-200 status code received: {r.status_code}")
        print(r.json())
        sys.exit(1)

    return r.json()

def create_lease_auth(url: str, auth, lease_id: str):
    r = requests.post(
        f"{url}/leases/{lease_id}/auth",
        auth=auth,
        timeout=5
    )

    if not r.ok:
        print(f"non-200 status code received: {r.status_code}")
        print(r.json())
        sys.exit(1)

    data = r.json()

    return {
        "credentials": {
            "access_key_id": data["accessKeyId"],
            "secret_access_key": data["secretAccessKey"],
            "session_token": data["sessionToken"]
        },
        "console_url": data["consoleUrl"],
        "lease_id": lease_id
    }
