#Arbitrary arguments (*args)
def sum(*num):
    total=0
    for i in num:
        total=total+i
    return total

print(sum(10,20,30,40,50))