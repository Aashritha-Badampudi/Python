def repeat(n):  # 1️⃣ Decorator argument
    
    def decorator(func):  # 2️⃣ Receives original function
        
        def wrapper(*args, **kwargs):  # 3️⃣ Wrapper
            for i in range(n):
                func(*args, **kwargs)
        
        return wrapper
    
    return decorator


@repeat(3)
def greet():
    print("Hello")

greet()