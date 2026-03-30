from users import *

user = User('andrii', 'popov', 'cossack', 1, 'aspidcg@gmail.com')

user.describe_user()
user.greet_user()

admin_user = Admin('alina', 'chernish', 'chalina', 0, 'chalina@gmail.com')
admin_user.describe_user()
admin_user.greet_user()

admin_user.pribilage.privilages()
admin_user.privilege.show_privileges()
