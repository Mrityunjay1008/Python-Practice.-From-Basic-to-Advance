class Employee:
    def __init__(self, first, last): 
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None
    
    
emp1 = Employee("Gopal", "Sharma")
emp1.first = "Ramlaal"

emp1.fullname = "Madan Sharma"
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
print(emp1.first)
print(emp1.last)