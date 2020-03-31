import json

def get_stored_username():
    filename='username.json'
    try:
        with open(filename) as f:
            usr=json.load(f)
    except FileNotFoundError:
        pass
    else:
        return usr

def get_new_username():
    usr=input('What is your name? ')
    filename='username.json'
    with open(filename, 'w') as f:
        json.dump(usr, f)
    return usr

def greet_user():
    usr=get_stored_username()
    if usr:
        print(f"Welcome back, {usr}!")
        x=input('Would you like to add another user? (yes/no): ')
        if x=='yes':
            usr=get_new_username()
            print(f"We'll remember when you come back, {usr}!")
    else:
        usr=get_new_username()
        print(f"We'll remember when you come back, {usr}!")

greet_user()