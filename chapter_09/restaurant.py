class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name.title()} has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is open")
        
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number


restaurants = [
                Restaurant("the mean queen", "pizza"),
                Restaurant("minani musashi", "sushi"),
                Restaurant("riso", "sushi"),
                Restaurant("mc donalds", "fast food"),
                Restaurant("idealist", "coffee"),
               ]

print(f"\nNumber served: {restaurants[0].number_served}")

restaurants[0].set_number_served(100)
print(f"Number served: {restaurants[0].number_served}")

restaurants[0].increment_number_served(2)
print(f"Number served: {restaurants[0].number_served}")

print("\n")
for r in restaurants:
    print(f"Restaurant name: {r.restaurant_name.title()}, Number served: {r.number_served}")