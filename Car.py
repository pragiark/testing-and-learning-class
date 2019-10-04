class Car():
    """Simple car class"""
    def __init__(self, make, model, year):
        """class atributies"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 800

    def get_descriptive_name(self):
        """Print car"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Add odometer method"""
        print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km.")

    def update_odometer(self, mileage):
        """Update odometer in method"""
        if mileage < self.odometer_reading:
            print("Nie mozna cofać licznika")
        else:
            self.odometer_reading = mileage



my_new_car = Car("ford", "focus", 2008)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(777)
#my_new_car.read_odometer()