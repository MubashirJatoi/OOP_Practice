class Employee:
    def __init__(self, emp_name: str, emp_ID: int):
        self.emp_name = emp_name
        self.emp_ID = emp_ID

    def display_info(self):
        print(f"Employee name: {self.emp_name}, ID: {self.emp_ID}")

class Department:
    def __init__(self, Dept_name: str, employee: Employee):
        self.Dept_name = Dept_name
        self.employee = employee

    def display_department_info(self):
        print(f"Department name: {self.Dept_name}")
        print("Employee Details:")
        self.employee.display_info()

emp1 = Employee("Mubashir", 104)

dept1 = Department("HR", emp1)

dept1.display_department_info()

emp1.display_info()