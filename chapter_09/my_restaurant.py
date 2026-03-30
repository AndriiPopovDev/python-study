from restaurant import Restaurant

my_restaurant = Restaurant('riso', 'sushi')

my_restaurant.describe_restaurant()
my_restaurant.served_number()

my_restaurant.set_number_served(4)
my_restaurant.served_number()

my_restaurant.increment_number_served(2)
my_restaurant.served_number()

my_restaurant.open_restaurant()