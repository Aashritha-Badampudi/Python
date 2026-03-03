#Decorator with arguements
def mulBy3(func):
    def wrapper(a,b):
        result = func(a,b)
        return result * 3
    return wrapper

@mulBy3
def add(a,b):
    return a+b

print(add(2,3))