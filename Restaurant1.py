class Restaurant():
    """Type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numeral_served = 0
        self.number_served = 0

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

    def read_number_served(self):
        """Method read numer served"""
        print("Liczba obsłużonych klientów wynosi: " + str(self.number_served))

    def set_number_served(self, client_served):
        """"Method add client served"""
        self.number_served += client_served

    def increment_served(self, increment_customer):
        """Increment served with secure"""
        self.number_served += increment_customer

restaurant = Restaurant("Goracy Piec", "Pizzeria")
restaurant.describe_restaurant()
restaurant.read_number_served()
restaurant.set_number_served(7)
restaurant.read_number_served()
restaurant.increment_served(20)
restaurant.read_number_served()
restaurant.increment_served(50)
restaurant.read_number_served()