class User():
    
    def __init__(self,
                first_name,
                last_name,
                username,
                id='',
                mail='',):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.id = id
        self.mail = mail

    def describe_user(self):
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"ID: {self.id}")
        print(f"Mail: {self.mail}")
    
    def greet_user(self):
        print(f"\nWerlcome back, {self.first_name} {self.last_name}!")
        

users = [User('alina', 'chernish', 'alicher', '150', 'alina@gmail.com'),
         User('andrii', 'popov', 'andriP', '151', 'andrii@gmail.com'),
         User('vlad', 'romanov', 'romashka', '152', 'vlad@gmail.com')]

for user in users:
    user.describe_user()
    user.greet_user()
    print('\n')