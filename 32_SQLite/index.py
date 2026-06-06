
class Employee:

    num_of_employees = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@gmail.com"
        self.pay = pay

        Employee.num_of_employees += 1

    def show_details(self):
        return f"Name: {self.first} {self.last}\nEmail: {self.email}\nPay: {self.pay}"
    
    def apply_raise(self):

        #OR
        self.pay = int(abs(self.pay)* self.raise_amount) 

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
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
    def __str__(self):
        return f"{self.first} {self.last} - {self.email}"