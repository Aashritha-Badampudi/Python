#Enclosing scope
def outer():
    x=20 #This is the enclosing variable ;)

    def inner():
        print(x)
    inner()

outer()