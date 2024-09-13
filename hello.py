from prefect import flow, task

@task
def create_message():
    msg = 'Hello from task'
    return msg

@flow
def something_else():
    result = 10
    return result

@flow
def hello_world():
    # Call the sub-flow and task, capturing their outputs
    sub_flow_message = something_else()
    task_message = create_message()

    # Combine messages
    new_message = task_message + str(sub_flow_message)

    # Return the final message
    return new_message
    
# Run the flow and capture the output
if __name__ == "__main__":
    output = hello_world()
    print("Final Output:", output)