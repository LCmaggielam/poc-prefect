from prefect_databricks import DatabricksCredentials

# Create the credentials block with required fields
credentials = DatabricksCredentials(
    host="https://adb-2661458153180226.6.azuredatabricks.net",  # Correct URL format
    token="dapi4d5c313e496ebec70d0f77afc2474391-2",  # Your actual token
    databricks_instance="adb-2661458153180226.6"  # Add the required instance field
)

# Save the credentials block
credentials.save("my-databricks-block")