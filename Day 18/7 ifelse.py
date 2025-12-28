""" Another condition in if-else i.e "if-elif-else"
Syntax : 
if condition1 :
    statement
elif condition2 :
    statement
else:
    statement """

marks=int(input("Enter the marks: \n"))
if marks >=90:
    print("Grade O")
elif marks>=80:
    print("Grade A")
elif marks >=60:
    print("Grade B")
if marks<=35:
    print("Fail")