from admin import Admin 

andrii = Admin('name', 'lastName', 'userName', 0, 'mail')
andrii.describe_user()

andrii_privileges = [
    'ban other users', 
    'send posts',
    'delete posts',
]
andrii.privileges.privileges = andrii_privileges
andrii.greet_user()
andrii.privileges.show_privileges()