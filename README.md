# poc-prefect
Schedule Databricks workflow to be run by Prefect

# How to execute
1. pip install -U Prefect
2. create a python file to create workflow and task on Prefect
3. prefect server start
   
# Deployment and Schedule flow
Please refer to the following link for further info on deployment on prefect workflow
https://docs.prefect.io/3.0/automate/add-schedules

# Apply on Databricks
1. Installation of prefect-databricks

https://docs.prefect.io/integrations/prefect-databricks/index


# Advantage comparing to Airflow
1. More clear UI, Some settings can be change and set up without coding(user-friendly for user dont have coding knowledge)
2. The Databricks token can be encrypted by using the block function in Prefect Server 

