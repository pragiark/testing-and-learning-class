import car

mondeo = car.Car("Ford", "Mondeo", 2017)
mondeo.get_descriptive_name()
prius = car.ElectricCar("Toyota", "Prius", 2012)
prius.get_descriptive_name()
prius.battery.describe_battery()
prius.battery.get_range()
