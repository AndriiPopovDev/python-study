class Users():
    def __init__(self, first_name, last_name, age=0, city=0, proffesion=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.proffesion = proffesion 

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} "
                f"is {self.age}, work {self.proffesion}, live in {self.city.title()}")
    
    def greet_user(self):
        print(f"Greetings, {self.first_name.title()} {self.last_name.title()}!")
        

andrii = Users('andrii', 'popov', 24, 'kyiv', 'coder')
alina = Users('alina', 'chernish', 24, 'kyiv', 'analyst')

andrii.describe_user()
andrii.greet_user()
print("\n")

alina.describe_user()
alina.greet_user()