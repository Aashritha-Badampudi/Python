#Hollow normal triangle/pyramid
n = 5
for i in range(1, n+1):
    for space in range(n-i):
        print("  ", end="")
    for star in range(2*i-1):
        if star == 0 or star == 2*i-2 or i == n:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
