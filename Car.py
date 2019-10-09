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



focus = Car("ford", "focus", 2008)
focus.get_descriptive_name()
#my_new_car.update_odometer(777)
focus.increment_odometer(77)
focus.read_odometer()
focus.fill_gas_tank(45)
focus.read_gas_tank()

tesla = ElectricCar("Tesla", "Model S", 2018)
tesla.get_descriptive_name()
tesla.read_odometer()
tesla.update_odometer(0)
tesla.read_odometer()
tesla.fill_gas_tank(20)
tesla.read_gas_tank()

tesla.battery.describe_battery()

