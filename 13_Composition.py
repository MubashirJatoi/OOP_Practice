class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()  

    def drive(self):
        self.engine.start()
        print("Car is driving")


my_car = Car()
my_car.drive()
