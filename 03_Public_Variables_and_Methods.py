class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print("Car is starting...")

car1 = Car("Toyota")

print(f"Car {car1.brand} is started.")