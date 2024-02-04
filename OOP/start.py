class Human:
    name = None
    age = None
    condition = None
    hight = None
    favorite_numbers = None

    def set_data(self, name, age):
        self.name = name
        self.age = age
        return
    
    def get_data(self):
        return f"{self.name}, age:, {self.age}, favorite_numbers: {self.favorite_numbers}"

Human1 = Human()
Human1.name = "Oleg"
Human1.age = 6
Human1.hight = 130.7
Human1.favorite_numbers = [10, 5, 7]

print(Human1.name)
print(Human1.favorite_numbers, "\n")

Human2 = Human()
Human2.set_data("user9397173...", 1247247923472717652)
print(Human2.name, Human2.age, sep="\n")

print()

print(Human1.get_data())
print(Human2.get_data())