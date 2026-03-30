from electric_car import ElectricCar as EC
 
my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.fill_gas_tank()

my_leaf.electric_motor.describe_motor()
my_leaf.electric_motor.ludicrous_mode()
my_leaf.electric_motor.ludicrous_mode()
