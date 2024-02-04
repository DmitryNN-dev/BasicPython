class Human:
    name = None
    age = None
    condition = None
    hight = None
    favorite_numbers = None

    def __init__(self, name=None, age=None, favorite_numbers=None):  # constructor
        self.name = name
        self.age = age
        self.favorite_numbers = favorite_numbers

        self.get_data()

    def get_data(self):
        print(f"{self.name}, age:, {self.age}, favorite_numbers: {self.favorite_numbers}")

new_Human = Human("Boris", 3294829, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])