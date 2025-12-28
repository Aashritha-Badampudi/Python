#Nested if else
age = int(input("Enter your age: \n"))
Ticket = input("Do you have ticket?(Answer in yes or no)\n")
if age >=18:
    if Ticket=="yes":
        print("Entry allowed")
    else:
        print("Not allowed")
else:
    print("Age less than 18 is not allowed")