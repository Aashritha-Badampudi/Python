import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return wrapper

@calculate_time
def slow_function():
    for i in range(1000000):
        pass

slow_function()