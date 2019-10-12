""""Class ElectricCar"""

from car import Car

class ElectricCar(Car):
    """Electric car class"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self, gas_tank):
        """No gas_tank information"""
        print("Nie dodam tego, elektryczny samochód nie ma zbiornika paliwa")

    def read_gas_tank(self):
        """No gas_tank information"""
        print("Elektryczny samochód nie posiada zbiornika paliwa")

class Battery():
    """Class battery to electric car"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        """"Print battery size information"""
        print("Ten samochód ma akumulator o pojemności " + str(self.battery_size) + " kWh")

    def get_range(self):
        """Range electric car"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        massage = "Zasięg wynosi około " + str(range)
        print(massage)