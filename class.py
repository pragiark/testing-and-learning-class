class Restaurant():
    """Type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numeral_served = 0

    def describe_restaurant(self):
        """Information"""
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restairant(self):
        """"Open hours"""
        print("Restaurant " + self.restaurant_name + " has open at: 6-22")

    def describe_served(self):
        """inform numer served"""
        print("Numer zamówienia " + str(self.numeral_served))

    def update_served(self, served):
        """update numer served"""
        self.numeral_served = served

    def set_number_served(self):
        """print served client"""
        print("Obsłużono: " + str(self.numeral_served) + " klientów")

    def increment_number_served(self, served):
        """Increment numer served"""
        self.numeral_served += served

restaurant = Restaurant("Goracy Piec", "Pizzeria")
restaurant.describe_served()
restaurant.update_served(7)
#restaurant.describe_served()
restaurant.set_number_served()
restaurant.increment_number_served(10)
restaurant.set_number_served()

#restaurant = restaurant.numeral_served = 20
#restaurant2 = Restaurant("Placek babuni", "Plackarnia")
#restaurant3 = Restaurant("Pierożek", "Bar Mleczny")

#restaurant1.describe_restaurant()
#restaurant2.describe_restaurant()
#restaurant3.describe_restaurant()

#restaurant.open_restairant()