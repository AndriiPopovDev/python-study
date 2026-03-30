from users import User

class Admin(User):
    def __init__(self, first_name, last_name, username, id, mail):
        super().__init__(first_name, last_name, username, id, mail)
        self.privileges = Privilege()


class Privilege():
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f" - {privilege}")
        else:
            print("- This user hasn't any privilages")
 