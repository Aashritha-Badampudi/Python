def decorator_function(func):
    
    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")
    
    return wrapper


@decorator_function
def greet(name):
    print("Hello", name)

greet("Honey")