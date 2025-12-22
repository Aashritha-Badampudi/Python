#Removing items from the dictionary
student = {"Name": "Aashritha", "Age" : 19, "Collage" : "SMEC"}

#Using pop() method
student.pop("Collage")
print(student)

#Using del[] method
del student["Age"]
print(student)

#Using clear() method
student.clear()
print(student)