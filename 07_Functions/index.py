def print_hello():
    print("Hello World")

print(print_hello) # this will print the function address
print_hello()

# Recursion(Calling a function inside a function)
def rec(i):
    if(i<0):
        return
    print(i)
    rec(i-1)

rec(5)

# Return and Perameters
def greeting(name):
    return f"Hello {name}"

print(greeting("Gopal"))
print(type(greeting("Gopal").upper()))

def add(num1, num2):
    return num1 + num2

print(add(10, 20))

# Default Perameters
def add(num1, num2=10):
    return num1 + num2

print(add(10))

# Arbitrary Perameters
def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))

# Keyword Perameters
def add(**kwargs):
    print(kwargs)
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum

print(add(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10))

def student_info(**kwargs):
    student = {}
    student.update(kwargs)
    return student

print(student_info(name="Gopal", age=21, course="Python", phone=1234567890, address="New Delhi", marks=90, grade="A"))

def student_database(*args, **kwargs):
    students = []
    student = {}
    for num in args:
        student.update(kwargs)
        students.insert(num,student)
    return students

print(student_database(0,1, name="Gopal", age=21, course="Python", phone=1234567890, address="New Delhi", marks=90, grade="A"))

user_info = {
    'name':"Gopal",
    'age':21,
    'email':"j5AeQ@example.com",
    'isLoggedIn':True
}
social_medias = ['instagram','facebook','twitter','linkedin']

def add_info(*args,**kargs):
    social_media = list(args)
    user = kargs
    user['social_media'] = social_media
    return user

print(add_info(*social_medias,**user_info))

years = [1996, 2000,2007, 2011, 2015, 2000, 2400, 1800, 1900, 2100]

def check_leap_year(year):
    if year <= 0:
        return False;
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
 
def print_leap_year(*args):
    for year in args:
        print(f"{year} is a {""if check_leap_year(year) else "not "}leap year")
    
print_leap_year(*years)
