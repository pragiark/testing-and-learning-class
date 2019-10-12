from car import Car
from electric_car import ElectricCar

mondeo = Car("Ford", "Mondeo", 2017)
mondeo.get_descriptive_name()
prius = ElectricCar("Toyota", "Prius", 2012)
prius.get_descriptive_name()
prius.battery.describe_battery()
prius.battery.get_range()
