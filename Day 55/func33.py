def example(a, *args, **kwargs):
    print("Normal:", a)
    print("Tuple:", args)
    print("Dictionary:", kwargs)

example(10, 20, 30, name="Honey", age=20)
