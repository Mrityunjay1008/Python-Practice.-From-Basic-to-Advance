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

    @classmethod # Alternate Constructor
    def set_raise_amount(cls,amount): 
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, arr):
        employees = []

        for emp_str in arr:
            first, last, pay = emp_str.split("-")
            employees.append(cls(first, last, pay))

        return employees
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee("Gopal", "Sharma",30000000)
emp2 = Employee("Ramlaal", "Sharma",20000000)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str_1 = "Ram-Sharma-30000000"
emp_str_2 = "Ramlaal-Sharma-20000000"
emp_str_3 = "Madan-Sharma-30000000"

emp_list = [emp_str_1,emp_str_2,emp_str_3]

[new_emp1,new_emp2,new_emp3] = Employee.from_string(emp_list)

print(new_emp1.show_details())
print(new_emp2.show_details())
print(new_emp3.show_details())

import datetime
my_date = datetime.date.today()

print(Employee.is_workday(my_date))