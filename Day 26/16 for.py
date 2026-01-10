#Loops with dictionaries
student={"name":"Aashritha","age":"19","course":"python"}
for i in student:
    print(i)
print("\n")
for val in student.values():
    print(val)
print("\n")
for i,val in student.items():
    print(i,":",val)