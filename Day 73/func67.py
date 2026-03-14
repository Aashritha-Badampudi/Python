#Lambda sorted()
pairs=[(1,3),(2,1),(4,2)]
result=sorted(pairs,key=lambda x:x[1]) #Storing is done based on second value
print(result)