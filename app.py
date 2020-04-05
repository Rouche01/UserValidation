import string
import random

users_list = {}


def prompt_new_user():
    input_first_name = input('Enter your first name here: ')
    input_last_name = input('Enter your last name here: ')
    input_email = input('Enter your email address here: ')
    create_user(input_first_name, input_last_name, input_email)


class Users:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def generate_password(self):
        password_random_strings = ''
        available_password_strings = string.ascii_letters + string.digits + string.punctuation
        for letter in range(5):
            password_random_strings += random.choice(available_password_strings)
        generated_password = self.first_name[:2] + self.last_name[-2:] + password_random_strings
        return generated_password


def create_user(f_name, l_name, email):
    new_user = Users(f_name, l_name, email)
    password = new_user.generate_password()
    print(f"We don't want you to go through the stress, so we generated a strong password for you: {password}")
    will_change_password = input('Are you satisfied with this password? Yes or No: ')
    while will_change_password.lower() != 'yes' and will_change_password.lower() != 'no':
        will_change_password = input('You have entered the wrong command? Expected answer is Yes or No: ')
    if will_change_password.lower() == 'yes':
        new_user.password = password
    elif will_change_password.lower() == 'no':
        changed_password = input('Enter your unique password (minimum of 7 characters): ')
        while len(changed_password) < 7:
            changed_password = input('Try again, the password must be equal to or greater than 7 in length: ')
        new_user.password = changed_password
    print(f'''
    First Name: {new_user.first_name}
    Last Name: {new_user.last_name}
    Email Address: {new_user.email}
    Password: {new_user.password}
    ''')

    full_name = new_user.first_name + " " + new_user.last_name
    users_list[full_name] = new_user


another_user = 'yes'
while another_user.lower() == 'yes':
    prompt_new_user()
    another_user = input('Another user? Yes or No: ')
    while another_user.lower() != 'yes' and another_user.lower() != 'no':
        another_user = input('You have entered the wrong command? Expected answer is Yes or No: ')
if another_user.lower() == 'no':
    for key, value in users_list.items():
        print(f'''
        {key}:
            First Name: {value.first_name}
            Last Name: {value.last_name}
            Email Address: {value.email}
            Password: {value.password}
        ''')
