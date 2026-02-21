x = 100

def outer():
    x = 50
    
    def inner():
        x = 10
        print(x)
    
    inner()

outer()