def outter_function(msg="hello"):
    
    def inner_function():
        print(msg)

    return inner_function


my_function = outter_function("Hello world")
my_function()

# What is a decorator?
# A decorator is a function that takes another function as an argument
# and returns a new function that adds extra functionality to the original function
# without modifying its source code.

def decorator_function(a=1,b=2,c=3):
    def inner_function():
        print(f"Average: {(a+b+c)/3}")
    return inner_function

my_function = decorator_function(1,2,93)
my_function()

def decorator_function(func):
    def inner_function(a,b,c):
        print(f"Average: {(a+b+c)/3}")
        func(a,b,c)
    return inner_function

def add_int(a,b,c):
    print(f"Sum: {a+b+c}")

my_function = decorator_function(add_int)
my_function(1,2,93)

def decorator_function(func):
    def inner_function(a,b,c):
        print()
        print("{} was called".format(func.__name__))
        func(a,b,c)
        print("End of {}".format(func.__name__))
        print()

    return inner_function

@decorator_function
def print_three_name(a,b,c):
    print("Start of print_three_name")
    print(a.upper())
    print(b.upper())
    print(c.upper())
    print("Three names printed")

print_three_name("Ramlaal","Phanalaal","Chandalaal")

user_info = {
    'name':"Gopal",
    'age':21,
    'email':"j5AeQ@example.com",
    'isLoggedIn':True
}
social_medias = ['instagram','facebook','twitter','linkedin']

def add_info_deco(fn):
    def inner_function(*args,**kargs):
        print()
        print(args)
        print(kargs)
        print()
        return fn(*args,**kargs)

    return inner_function

@add_info_deco
def add_info(*args,**kargs):
    social_media = list(args)
    user = kargs
    user['social_media'] = social_media
    return user

print(add_info(*social_medias,**user_info))

# Class Decorators

class Decorators_class(object):
    def __init__(self,fn):
        self.fn = fn

    def __call__(self,*args,**kargs):
        print()
        print(args)
        print(kargs)
        print()
        return self.fn(*args,**kargs)
    

@Decorators_class
def add_info(*args,**kargs):
    social_media = list(args)
    user = kargs
    user['social_media'] = social_media
    return user

print(add_info(*social_medias,**user_info))

# Real life use case

data_base = [

    {
        "name": "Gopal",
        "age": 21,
        "email": "j5AeQ@example.com",
        "isLoggedIn": True
    },
    {
        "name": "Priya",
        "age": 19,
        "email": "priya.verma@example.com",
        "isLoggedIn": False
    },
    {
        "name": "Rahul",
        "age": 25,
        "email": "rahul.singh@example.com",
        "isLoggedIn": True
    },
    {
        "name": "Ananya",
        "age": 22,
        "email": "ananya.sharma@example.com",
        "isLoggedIn": True
    },
    {
        "name": "Vikram",
        "age": 28,
        "email": "vikram.patel@example.com",
        "isLoggedIn": False
    },
]

def edit_user_decorator(func):
    def inner_function(index,**kargs):
        if (index<0 or index>len(data_base)-1) or type (index) != int:
            raise Exception("Invalid index")
        if not data_base[index]["isLoggedIn"]:
            raise Exception("User is not authenticated")
        if "isLoggedIn" in kargs:
            raise Exception("You can not update your login status")
        result = func(index,**kargs)
        if(not result["success"]):
            raise Exception(result["message"])
        print(result["message"])
        print(f'\n{result["user"]}\n')
    return inner_function

@edit_user_decorator
def update_user(index,**kargs):
    try:
        data_base[index].update(kargs)
        return {
            "user":data_base[index],
            "success":True,
            "message":"User updated successfully"
        }
    except Exception as e:
        return {
            "user":None,
            "success":False,
            "message":str(e)
        }
    

update_user(0,name="Gopal Sharma",email="sharmagopal1306@example.com")
