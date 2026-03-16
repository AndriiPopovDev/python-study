class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is open")


riso = Restaurant("riso", "sushi")
mcdonalds = Restaurant("mc donalds", "fast food")
idealist = Restaurant("idealist", "coffee")

riso.describe_restaurant()
riso.open_restaurant()

print("\n")
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()

print("\n")
idealist.describe_restaurant()
idealist.open_restaurant()