from hubspot import fetch_hubspot_contacts
from apollo import fetch_apollo_users
from salesforce import fetch_salesforce_contacts
from snowflake_load import create_snowflake_session, upload_dataframe_to_snowflake

def main():
    print("Fetching HubSpot contacts...")
    hubspot_df = fetch_hubspot_contacts()

    print("Fetching Apollo users...")
    apollo_df = fetch_apollo_users()

    print("Fetching Salesforce contacts...")
    salesforce_df = fetch_salesforce_contacts()

    print("Creating Snowflake session...")
    session = create_snowflake_session()

    print("Uploading HubSpot data...")
    upload_dataframe_to_snowflake(session, hubspot_df, "HUBSPOT_CONTACTS")

    print("Uploading Apollo data...")
    upload_dataframe_to_snowflake(session, apollo_df, "APOLLO_USERS")

    print("Uploading Salesforce data...")
    upload_dataframe_to_snowflake(session, salesforce_df, "SALESFORCE_CONTACTS")

    session.close()
    print("All data uploaded successfully!")

if __name__ == "__main__":
    main()
