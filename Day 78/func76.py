#Generators
def my_gnrtr():
    yield 1
    yield 5
    yield 3

for value in my_gnrtr():
    print(value)