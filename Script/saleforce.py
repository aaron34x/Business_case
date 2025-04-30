from simple_salesforce import Salesforce
import pandas as pd

# credentials
sf_username = 'your_salesforce_username'
sf_password = 'your_salesforce_password'
sf_security_token = 'your_salesforce_security_token'
sf_client_id = 'your_connected_app_client_id'
sf_client_secret = 'your_connected_app_client_secret'

def fetch_salesforce_contacts():
    sf = Salesforce(
        username=sf_username,
        password=sf_password,
        security_token=sf_security_token,
        client_id=sf_client_id,
        client_secret=sf_client_secret
    )

    
    query = "SELECT Id, FirstName, LastName, Email FROM Contact LIMIT 100"
    results = sf.query(query)

    records = results.get('records', [])
    
    # Convert to  DataFrame
    rows = []
    for rec in records:
        rows.append({
            'Id': rec.get('Id'),
            'FirstName': rec.get('FirstName'),
            'LastName': rec.get('LastName'),
            'Email': rec.get('Email'),
        })

    return pd.DataFrame(rows)
