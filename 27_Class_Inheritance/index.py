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
    

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.show_details())

dev_1 = Developer("Gopal", "Sharma", 30000000, "Python")
dev_2 = Developer("Ramlaal", "Sharma", -20000000, "Java")

print("###############DEV1###############")
print(dev_1.show_details())
dev_1.apply_raise()
print(dev_1.show_details())

Mrittunjay = Manager("Mritunjay", "Sharma", 50000000, [dev_1])
print("###############MRITYUNJAY###############")
print(Mrittunjay.show_details())
Mrittunjay.add_emp(dev_2)
Mrittunjay.remove_emp(dev_2)
Mrittunjay.print_emps()

print(isinstance(Mrittunjay, Manager)) # True
print(isinstance(Mrittunjay, Employee)) # True
print(isinstance(Mrittunjay, Developer)) # False