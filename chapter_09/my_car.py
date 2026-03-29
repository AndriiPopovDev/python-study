from car import Car

my_new_car = Car('honda', 'civic', 2004)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometr(25)
my_new_car.read_odometr()