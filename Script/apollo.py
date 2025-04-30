import requests
import pandas as pd

APOLLO_API_KEY = "YOUR_API_KEY_HERE"

def fetch_apollo_users():
    url = "https://api.apollo.io/v1/users/search"
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'X-Api-Key': APOLLO_API_KEY
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    users = data.get("users", [])
    rows = []
    for user in users:
        rows.append({
            'first_name': user.get('first_name'),
            'last_name': user.get('last_name'),
            'email': user.get('email')
        })
    return pd.DataFrame(rows)
