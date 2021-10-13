import time

def calculate_time(func):
    def test_decorator():
        start_time= time.time()
        test_function()
        end_time=time.time()
        total_time= end_time-start_time
        print ("Total time ",total_time)
    return test_decorator
def test_function():
    time.sleep(1)
    time.sleep(2)

final_runtime=calculate_time(test_function)
final_runtime()
