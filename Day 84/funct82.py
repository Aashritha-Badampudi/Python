def my_gen():
  try:
    yield 1
    yield 4
    yield 2
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
