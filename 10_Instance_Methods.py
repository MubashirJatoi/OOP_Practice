class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Wooff!")

my_dog = Dog("Gang", "Cyberian Husky")

my_dog.bark()