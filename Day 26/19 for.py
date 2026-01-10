#else and break in for loop
for i in range(1,6):
    if i==5:
        break
    print(i)
else:
    print("Loop completed.")