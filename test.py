from prefect import flow
from prefect_databricks import DatabricksCredentials
from prefect_databricks.flows import jobs_runs_submit_and_wait_for_completion
from prefect_databricks.models.jobs import (
    AutoScale,
    AwsAttributes,
    JobTaskSettings,
    NotebookTask,
    NewCluster,
)


@flow
def jobs_runs_submit_flow(block_name: str, notebook_path: str, **base_parameters):
    databricks_credentials = (
        host="https://adb-2661458153180226.6.azuredatabricks.net",  # Correct URL format
    token="dapi4d5c313e496ebec70d0f77afc2474391-2"
    )

    # specify new cluster settings
    aws_attributes = AwsAttributes(
        availability="SPOT",
        zone_id="us-west-2a",
        ebs_volume_type="GENERAL_PURPOSE_SSD",
        ebs_volume_count=3,
        ebs_volume_size=100,
    )
    auto_scale = AutoScale(min_workers=1, max_workers=2)
    new_cluster = NewCluster(
        aws_attributes=aws_attributes,
        autoscale=auto_scale,
        node_type_id="m4.large",
        spark_version="10.4.x-scala2.12",
        spark_conf={"spark.speculation": True},
    )

    # specify notebook to use and parameters to pass
    notebook_task = NotebookTask(
        notebook_path=notebook_path,
        base_parameters=base_parameters,
    )

    # compile job task settings
    job_task_settings = JobTaskSettings(
        new_cluster=new_cluster,
        notebook_task=notebook_task,
        task_key="prefect-task"
    )

    run = jobs_runs_submit_and_wait_for_completion(
        databricks_credentials=databricks_credentials,
        run_name="prefect-job",
        tasks=[job_task_settings]
    )

    return run


jobs_runs_submit_flow(
    block_name="BLOCK-NAME-PLACEHOLDER"
    notebook_path="/Users/<EMAIL_ADDRESS_PLACEHOLDER>/example.ipynb",
    name="Marvin"
)