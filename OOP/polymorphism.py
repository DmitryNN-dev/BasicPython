class Buildinig:
    year = None
    city = None

    def __init__(self, build_name, year, city):
        self.build_name = build_name
        self.year = year
        self.city = city
    
    def get_info(self):
        print(f"Build_name: {self.build_name}; Year: {self.year}; City: {self.city}")

school = Buildinig("School", 2000, "Moscow")
house = Buildinig("House", 2000, "Moscow")
shop = Buildinig("Shop", 2000, "Moscow")

# 

class School(Buildinig):
    people = 0

    def __init__(self, build_name, people, year, city):
        super(School, self).__init__(build_name, year, city)
        self.people = people

    def get_info(self):
        super().get_info()
        print("People:", self.people)
    pass

class House(Buildinig):
    pass

school1 = School("first_school", 150, 2000, "Moscow")
school1.get_info()