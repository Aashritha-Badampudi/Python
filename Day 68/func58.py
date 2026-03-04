def multiply(n):
    def decorator(func):
        def wrapper(a, b):
            return func(a, b) * n
        return wrapper
    return decorator

@multiply(5)
def add(a, b):
    return a + b

print(add(2, 3))