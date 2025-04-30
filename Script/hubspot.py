import requests
import pandas as pd

HUBSPOT_API_KEY = "YOUR_HUBSPOT_API_KEY"

def fetch_hubspot_contacts():
    url = f"https://api.hubapi.com/contacts/v1/lists/all/contacts/all?hapikey={HUBSPOT_API_KEY}&count=100"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    contacts = data.get("contacts", [])
    rows = []
    for c in contacts:
        vid = c.get("vid")
        props = c.get("properties", {})
        rows.append({
            'vid': vid,
            'email': props.get('email', {}).get('value'),
            'firstname': props.get('firstname', {}).get('value'),
            'lastname': props.get('lastname', {}).get('value'),
        })
    return pd.DataFrame(rows)
