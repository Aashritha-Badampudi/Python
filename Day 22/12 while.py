#Count the digits using while loop
num=int(input("Enter your number: \n"))
count=0
while num!=0:
    num=num//10
    count=count+1

print(count)