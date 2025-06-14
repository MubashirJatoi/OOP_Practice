class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError
    else:
        print("Access granted. Age is valid")
    
try:
    user_age = int(input("what is your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid number.")