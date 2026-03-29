import electric_car

"""A class that can be use to represent a car"""

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


       
    
if __name__ == "__main__":
    my_new_car = Car('audi', 'a4', 2016)
    tesla = electric_car.ElectricCar('tesla', 'model s', 2016)
    leaf = electric_car.ElectricCar('nissan', 'leaf', 2024)

    print(my_new_car.get_descriptive_name()) 
    print(tesla.get_descriptive_name())
    tesla.battery.describe_battery()
    leaf.battery.describe_battery()
    leaf.battery.get_range()
    leaf.battery.upgrade_battery()
    leaf.battery.describe_battery()