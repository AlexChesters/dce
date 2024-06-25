import requests
import inquirer

def list_accounts(url, auth):
    r = requests.get(url=f"{url}/accounts", auth=auth, timeout=5)
    r.raise_for_status()

    return r.json()

def add_account(url, auth):
    answers = inquirer.prompt([inquirer.Text("account_id", message="What is the account ID?")])

    account_id = str(answers["account_id"])
    body = {
        "id": account_id,
        "adminRoleArn": f"arn:aws:iam::{account_id}:role/DCEAdmin",
    }

    print(body)

    r = requests.post(
        f"{url}/accounts",
        auth=auth,
        timeout=5,
        json=body
    )
    r.raise_for_status()

    return r.json()
