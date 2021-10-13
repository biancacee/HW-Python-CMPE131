import time

def calculate_time(func):
        start_time= time.time()
        test_function()
        end_time=time.time()
        total_time= end_time-start_time
        print ("Total time {}".format(total_time))
def test_function():
    time.sleep(2)

calculate_time(test_function)
