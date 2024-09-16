from prefect_databricks import DatabricksCredentials

# Create a DatabricksCredentials block (if not already created)
databricks_credentials = DatabricksCredentials(
    host="https://adb-<workspace-id>.azuredatabricks.net",
    token="dapid1f5f53a969f0c390204b06b55b53902-2"
)

# Save the block
databricks_credentials.save("my-databrickv3")