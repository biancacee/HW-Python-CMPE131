import time

def calculate_time(test_function):
    """This function takes in a function, keeps track of it's start time and end time to then determine the runtime of that function. The nested function within the decorator returns the total time the passed function takes to run. """
    def wrapper():
        start_time= time.time() #keep track of start time
        test_function()
        end_time=time.time() #keep track of end time
        total_time= end_time-start_time #do the math to find total runtime
        print("Total time {}".format(total_time))
    return wrapper


