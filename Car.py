class Car():
    """Simple car class"""
    def __init__(self, make, model, year):
        """class atributies"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Print car"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car("ford", "focus", 2008)
print(my_new_car.get_descriptive_name())