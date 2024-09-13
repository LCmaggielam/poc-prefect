from prefect import flow
from prefect_databricks import DatabricksCredentials

@flow
def create_databricks_block():
    # Create the credentials block
    databricks_credentials = DatabricksCredentials(
        databricks_instance="https://adb-2661458153180226.6.azuredatabricks.net",
        token="dapi4d5c313e496ebec70d0f77afc2474391-2"
    )
    
    # Save the credentials block
    databricks_credentials.save("databricks-block")  # Replace with your desired block name

if __name__ == "__main__":
    create_databricks_block()