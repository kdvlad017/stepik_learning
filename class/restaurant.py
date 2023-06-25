class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type} {self.number_served}")

    def open_restaurant(self=None):
        print(f"Restaurant {self.restaurant_name} is open")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = flavors

    def flavors_list(self):
        print(self.flavors)