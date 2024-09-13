from prefect import flow, task
from prefect_databricks import DatabricksCredentials

@task
def get_databricks_credentials():
    # Load the Databricks credentials block
    databricks_credentials = DatabricksCredentials.load("databricks-block")  # Replace with your block name
    
    # Access the databricks_instance and token
    instance = databricks_credentials.databricks_instance
    token = databricks_credentials.token
    
    print(f"Databricks Instance: {instance}")
    print(f"Token: {token}")
    
    return instance, token

@flow
def databricks_workflow():
    get_databricks_credentials()

if __name__ == "__main__":
    databricks_workflow()