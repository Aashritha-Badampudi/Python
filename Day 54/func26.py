#Largest of 2 numbers
def greater(a,b):
    if a>b:
        return a
    elif a==b:
        return ("Equal")
    else:
        return b
    
print(greater(25,70))
print(greater(100,100))
print(greater(20,13))