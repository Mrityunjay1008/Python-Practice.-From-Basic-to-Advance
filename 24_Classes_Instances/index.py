# Python Object Oriented Programming
# Method: method is a function associated with a class
# Class is a blueprint for creating Instances
class Employee:
    def __init__(self, first, last, pay): # Constructor, where self is the instance
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

    def show_details(self): # Method, where self is important
        return f"Name: {self.first} {self.last}\nEmail: {self.email}\nPay: {self.pay}"

# These both are instances of the Employee class
emp1 = Employee("Gopal", "Sharma","3cr")
emp2 = Employee("Ramlaal", "Sharma","2cr")

# NOT important
emp1.first = "Gopal"
emp1.last = "Sharma"
emp1.email = "j5AeQ@example.com"
emp1.pay = "3cr"

emp2.first = "Ramlaal"
emp2.last = "Sharma"
emp2.email = "ABC@example.com"
emp2.pay = "2cr"

print(emp1.show_details())
print()
print(emp2.show_details())
# OR
print(Employee.show_details(emp1))
print()
print(Employee.show_details(emp2))