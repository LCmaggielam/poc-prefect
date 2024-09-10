from prefect import flow, task

@task
def create_message():
    msg = 'Hello from task'
    return(msg)


@flow
def something_else():
    result = 10
    return(result)

@flow
def hello_world():
    sub_flow_message = something_else()
    task_message = create_message()
    new_message = task_message + str(sub_flow_message)
    print(new_message)
    
hello_world()