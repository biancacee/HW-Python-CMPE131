import time

def calculate_time(func):
    time_seconds = time.time()
    print("Total time", time_seconds)
calculate_time(time.sleep(2))
