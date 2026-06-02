class Employee:

    num_of_employees = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

        Employee.num_of_employees += 1

    def show_details(self):
        return f"Name: {self.first} {self.last}\nEmail: {self.email}\nPay: {self.pay}"
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) 
        #OR
        self.pay = int(self.pay * self.raise_amount) 



emp1 = Employee("Gopal", "Sharma",30000000)
emp2 = Employee("Ramlaal", "Sharma",20000000)

print(emp1.show_details())
emp1.apply_raise()
print(emp1.show_details())

print(emp1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05
emp1.raise_amount = 1.06

print(Employee.num_of_employees)