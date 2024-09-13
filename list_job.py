import requests
from prefect import flow, task
from prefect_databricks import DatabricksCredentials

@task
def test_databricks_connection():
    databricks_credentials = DatabricksCredentials.load("my-databricks-block")
    host = "https://adb-2661458153180226.6.azuredatabricks.net"
    token = "dapi4d5c313e496ebec70d0f77afc2474391-2"
    
    if not host or not token:
        print("Failed to retrieve host or token from credentials.")
        return False
    
    return True

@task
def list_databricks_jobs():
    databricks_credentials = DatabricksCredentials.load("my-databricks-block")
    host = "https://adb-2661458153180226.6.azuredatabricks.net"
    
    token = "dapi4d5c313e496ebec70d0f77afc2474391-2"
    print(token)

    url = f"{host}/api/2.0/jobs/list"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        jobs = response.json().get('jobs', [])
        print("Databricks Jobs:")
        for job in jobs:
            print(f"Job ID: {job['job_id']}, Job Name: {job['settings']['name']}")
        return jobs
    except Exception as e:
        print("Failed to list jobs:", e)
        return None

@flow
def databricks_workflow():
    if test_databricks_connection():
        print("Successfully connected to Databricks.")
        list_databricks_jobs()
    else:
        print("Failed to connect to Databricks.")

if __name__ == "__main__":
    databricks_workflow()