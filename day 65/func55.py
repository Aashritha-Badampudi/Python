def simple_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@simple_decorator
def greet():
    print("Hello Python")

greet()