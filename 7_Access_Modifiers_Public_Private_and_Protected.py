class Employee:

    name = "Mubashir"

    _salary = 10000

    __ssn = "12-12-2006"

emp = Employee()

print(f"Name: {emp.name}")

print(f"Salary: {emp._salary}")

try:
    print(f"SSN: {emp.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")

print(f"SSN (via name mangling): {emp._Employee__ssn}")