import requests
from prefect import flow, task
from prefect_databricks import DatabricksCredentials

@task
def test_databricks_connection():
    # Load the Databricks credentials from the Prefect block
    databricks_credentials = DatabricksCredentials.load("my-block")
    
    # Access the host and token from the block's __dict__
    host = databricks_credentials.__dict__.get("host")
    token = databricks_credentials.__dict__.get("token")
    
    if not host or not token:
        print("Failed to retrieve host or token from credentials.")
        return False
    
    # Prepare the API endpoint for listing clusters
    url = f"{host}/api/2.0/clusters/list"
    
    # Set the headers for the request
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Attempt to make the API request
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        clusters = response.json()
        print("Clusters:", clusters)
        return True
    except Exception as e:
        print("Connection failed:", e)
        return False

@flow
def check_connection_flow():
    connection_status = test_databricks_connection()
    if connection_status:
        print("Successfully connected to Databricks.")
    else:
        print("Failed to connect to Databricks.")

if __name__ == "__main__":
    check_connection_flow()