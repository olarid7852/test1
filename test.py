class MyGenerator:
    def __init__(self, max_value):
        self.max_value = max_value

    def __iter__(self):
        for i in range(1, self.max_value + 1):
            yield i


my_gen = MyGenerator(5)
for value in my_gen:
    print(value)  # prints 1, 2, 3, 4, 5
