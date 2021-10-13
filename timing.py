import time

def calculate_time(func):
    def test_decorator():
        start_time= time.time()
        test_function()
        end_time=time.time()
        total_time= end_time-start_time
        print ("Total time ",total_time)
    return test_decorator
