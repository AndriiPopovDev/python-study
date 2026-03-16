class User():
    
    def __init__(self,
                first_name,
                last_name,
                password='',
                id='',
                mail='',):
        
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.id = id
        self.mail = mail

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
    
    def greet_user(self):
        print(f"Greetings, {self.first_name.title()} {self.last_name.title()}!")
        

users = [User('alina', 'chernish'),
         User('andrii', 'popov'),
         User('vlad', 'romanov')]

for user in users:
    user.describe_user()
    user.greet_user()
    print('\n')