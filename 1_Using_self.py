class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student {self.name} got {self.marks} marks")
    
student1 = Student("Mubashir", 12)
print(student1.display())