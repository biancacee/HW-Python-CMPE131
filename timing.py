import time

def calculate_time(test_function):
    def wrapper():
        start_time= time.time()
        test_function()
        end_time=time.time()
        total_time= end_time-start_time
        print("Total time is ", total_time)
    return wrapper

def function_runtime():
    time.sleep(2)

function_runtime=calculate_time(function_runtime)
function_runtime()
