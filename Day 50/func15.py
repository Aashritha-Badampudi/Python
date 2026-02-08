def largest(a, b, c):
    if a >= b and a >= c:
        print(a, "is largest")
    elif b >= a and b >= c:
        print(b, "is largest")
    else:
        print(c, "is largest")

largest(4, 9, 2)
