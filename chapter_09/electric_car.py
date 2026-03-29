"""A set of classes that can be used to represent electric cars"""

from car import Car

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Tnan initialize specific attributes for the electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        self.electric_motor = ElectricMotor()

    def fill_gas_tank(self):
        """Electric cars don't have a gas tank"""
        print("This car doesn't have a gas tank")

    
class Battery:
        """A simple attempt to model a battery for an electric car"""
        def __init__(self, battery_size=40):
            """Initialize the battery attributes"""
            self.battery_size = battery_size

        def describe_battery(self):
            """Print a statement to describe the battery size"""
            print(f"Battery size: {self.battery_size}-kW battery")

        def get_range(self, range=0):
            """Print a statement about the range this battery provides"""
            if self.battery_size == 40:
                range = 150
            elif self.battery_size == 65:
                range = 225

            print(f"This car can go about {range} miles on a full charge")
                
        def upgrade_battery(self):
            if self.battery_size == 40:
                self.battery_size = 65
                print("\nUpgraded the battery to 65kWh")
            else:
                print("Your battery already update!")
 

class ElectricMotor:
    def __init__(self, horsepower=150):
        """Initialize the horsepower attribute"""
        self.horsepower = horsepower

    def describe_motor(self):
        print(f"This car has a {self.horsepower}-HP electric motor")

    def ludicrous_mode(self):
        if self.horsepower < 500:
            self.horsepower = 500
            print("ludicrous mode activated, horsepower bosted to 500 HP")
        else:
            print("ludicrous mode is already active")
        