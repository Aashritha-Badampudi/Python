#Challenges started
username=input("Enter the username\n")
password=int(input("Enter your password\n"))

if username=="admin" and password==1234:
    print("Login successful")
else:
    print("Incorrect credentials")