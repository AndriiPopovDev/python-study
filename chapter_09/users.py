class User():
    def __init__(self,
                first_name,
                last_name,
                username,
                id,
                mail,):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.id = id
        self.mail = mail
        self.loggin_attempts = 0

    def describe_user(self):
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"ID: {self.id}")
        print(f"Mail: {self.mail}")
    
    def greet_user(self):
        print(f"\nWerlcome back, {self.first_name} {self.last_name}!")

    def increment_loggin_attempts(self):
        self.loggin_attempts += 1

    def reset_loggin_attempts(self):
        self.loggin_attempts = 0

        
class Admin(User):
    def __init__(self, first_name, last_name, username, id, mail):
        super().__init__(first_name, last_name, username, id, mail)
        self.privileges = Privilege()


class Privilege():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f" - {privilege}")
        else:
            print("This user hasn't any privilages")
    

if __name__ == "__main__":
    users = [User('alina', 'chernish', 'alicher', '150', 'alina@gmail.com'),
            User('andrii', 'popov', 'andriP', '151', 'andrii@gmail.com'),
            User('vlad', 'romanov', 'romashka', '152', 'vlad@gmail.com')]

    andrii = Admin('andrii', 'popov', 'andriipopov', '1', 'andrii@gmail.com')
    andrii.describe_user()


    andrii.privileges.show_privileges()
    print("\nAdding privilages...")

    andrii_privileges = [
        'can add post',
        'can delete post', 
        'can ban user'
    ]
    andrii.privileges.privileges = andrii_privileges
    andrii.privileges.show_privileges()


    users[2].describe_user()
    print(f"\nLoggin attempts: {users[2].loggin_attempts}")

    users[2].increment_loggin_attempts()
    users[2].increment_loggin_attempts()
    users[2].increment_loggin_attempts()
    print(f"\nLoggin attempts: {users[2].loggin_attempts}")

    users[2].reset_loggin_attempts()
    print(f"loggin attempts: {users[2].loggin_attempts}")
