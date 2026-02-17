#Checking prime
def is_prime(num):
    if num<=1:
        return "Not prime"
    for i in range(2,num):
        if num%i==0:
            return "Not prime"
        else:
            return "Prime" 
print(is_prime(7))
print(is_prime(4))
print(is_prime(-8))