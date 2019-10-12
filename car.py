"""Class Car"""

class Car():
    """Simple car class"""
    def __init__(self, make, model, year):
        """class atributies"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Print car"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        print(long_name.title())

    def read_odometer(self):
        """Add odometer method"""
        print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km.")

    def update_odometer(self, mileage):
        """Update odometer in method"""
        if mileage < self.odometer_reading:
            print("Nie mozna cofać licznika")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, kilometer):
        """Increment odometer method"""
        self.odometer_reading += kilometer

    def fill_gas_tank(self, gas_tank):
        """Add gas tank"""
        self.gas_tank = gas_tank

    def read_gas_tank(self):
        """"Print gas tank"""
        print(self.make + ", " + self.model + " ma zbiornik paliwa o pojemności " + str(self.gas_tank) + " litrów")

