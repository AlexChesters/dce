import requests

def list_accounts(url, auth):
    r = requests.get(url=f"{url}/accounts", auth=auth, timeout=5)
    r.raise_for_status()

    return r.json()

def add_account(url, auth, account_id):
    body = {
        "id": account_id,
        "adminRoleArn": f"arn:aws:iam::{account_id}:role/DCEAdmin",
    }

    r = requests.post(
        f"{url}/accounts",
        auth=auth,
        timeout=5,
        json=body
    )
    r.raise_for_status()

    return r.json()

def delete_account(url, auth, account_id):
    r = requests.delete(
        f"{url}/accounts/{account_id}",
        auth=auth,
        timeout=5
    )
    r.raise_for_status()

    return r.status_code
