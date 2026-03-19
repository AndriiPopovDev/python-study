class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometr(self, mileage):
        """
        Set the odometr reading to the given value.
        Reject the change if it attempts to roll the odometr back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year, battery_size=0):
        """
        Initialize attributes of the parent class
        Tnan initialize specific attributes for the electric car
        """
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size} kWh battery")

my_new_car = Car('audi', 'a4', 2016)
tesla = ElectricCar('tesla', 'model s', 2016, 85)

print(my_new_car.get_descriptive_name()) 
print(tesla.get_descriptive_name())
tesla.describe_battery()


"""
my_new_car.read_odometr()

my_new_car.update_odometr(432)
my_new_car.read_odometr()
my_new_car.update_odometr(300)

my_new_car.increment_odometer(100)
my_new_car.read_odometr()
"""