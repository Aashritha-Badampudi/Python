# Manual decorator
def decorator_function(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


def greet():
    print("Hello")

greet = decorator_function(greet)

greet()