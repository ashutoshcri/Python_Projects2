class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"\nName of the restaurant is {self.restaurant_name}.")
        print(f"Name of the cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,served):
        self.number_served=served

    def increment_number_served(self,incr_served):
        self.number_served+=incr_served

restaurant=Restaurant('The Big Wok','French Fries')
restaurant.set_number_served(59)
restaurant.increment_number_served(10)
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")