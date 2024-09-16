import requests
from prefect import flow, task
from prefect_databricks import DatabricksCredentials
from pydantic import BaseModel, SecretStr


@task
def test_databricks_connection():
    databricks_credentials = DatabricksCredentials.load("my-databrickv2")
    host = "https://adb-2661458153180226.6.azuredatabricks.net"
    token ="dapi4d5c313e496ebec70d0f77afc2474391-2"
    
    if not host or not token:
        print("Failed to retrieve host or token from credentials.")
        return False
    
    return True

@task
def list_databricks_jobs():
    databricks_credentials = DatabricksCredentials.load("my-databrickv2")
    host = databricks_credentials.databricks_instance
    
    #token = "dapi4d5c313e496ebec70d0f77afc2474391-2"
    token = databricks_credentials.token
    print(type(token))
    #print(f"Using token: {token}")
    
    if isinstance(token, SecretStr):
        token = token.get_secret_value()  # Convert to string

    #print(f"Using token: {token}")

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
        return jobs  # Return the list of jobs
    except Exception as e:
        print("Failed to list jobs:", e)
        return None

@task
def run_databricks_job(job_id):
    databricks_credentials = DatabricksCredentials.load("my-databrickv2")
    host = databricks_credentials.databricks_instance
    
    token = "dapi4d5c313e496ebec70d0f77afc2474391-2"
    url = f"{host}/api/2.0/jobs/run-now"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "job_id": job_id
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        run_info = response.json()
        print(f"Job {job_id} started successfully: {run_info}")
        return run_info
    except Exception as e:
        print("Failed to run job:", e)
        return None

@flow(name="S_OOMS_flow")
def databricks_workflow():
    if test_databricks_connection():
        print("Successfully connected to Databricks.")
        jobs = list_databricks_jobs()  # Get the list of jobs
        if jobs:
            # For example, run the first job in the list
            job_id_to_run = 1092601105688152  # Change index as needed
            run_databricks_job(job_id_to_run)
    else:
        print("Failed to connect to Databricks.")
        

if __name__ == "__main__":
    databricks_workflow.serve(
        name="s-ooms-deployment",
        cron="0 7 * * *",  # Set to run at 7:00 AM every day
        tags=["testing", "tutorial"],
        description="Given a GitHub repository, logs repository statistics for that repo.",
        version="tutorial/deployments",
    )