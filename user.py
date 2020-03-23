class User:
    def __init__(self,first_name,last_name,age,city):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.city=city
        self.login_attempts=0

    def describe_user(self):
        print(f"\nFist name of the user is {self.first_name}.")
        print(f"Last name of the user is {self.last_name}.")
        print(f"Age of the user is {self.age}.")
        print(f"City of the user is {self.city}.")

    def greet_user(self):
        print(f"\nWelcome {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

user=User('Nick','Jonas',27,'New York')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts are {user.login_attempts}.")
user.reset_login_attempts()
print(f"Login attempts reset to {user.login_attempts}.")