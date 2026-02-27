#Using @syntax
def decorator_function(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@decorator_function
def greet():
    print("Hello")

greet()