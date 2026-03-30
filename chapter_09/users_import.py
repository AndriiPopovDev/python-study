from users import *

user = User('andrii', 'popov', 'cossack', 1, 'aspidcg@gmail.com')

user.describe_user()
user.greet_user()

admin_user = Admin('alina', 'chernish', 'chalina', 0, 'chalina@gmail.com')
admin_user.describe_user()
admin_user.greet_user()

admin_user_privileges = [
    'send message',
    'delete message', 
    'ban users'
]

admin_user.privileges.privileges = admin_user_privileges
admin_user.privileges.show_privileges()
