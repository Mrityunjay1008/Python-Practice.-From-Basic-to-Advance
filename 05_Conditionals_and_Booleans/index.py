"""
if(Any condition):
    if that condition is true:
        do something
elif(Any other condition):
    if that condition is true:
        do something else
else:
    do something else

"""

name = "Gopal"
age = 18
age1 = 21
language = "Python"

user = {
    'username':"john doe",
    'age':21,
    "isLoggedIn":True,
    "role":"admin",
    "token":"this is a very complex token"
}

# Basic Checks
if(name == "Gopal"):
    print("Your name is Gopal")
else:
    print("Your name is not Gopal")

if(age == 18):
    print("You are 18 years old")
else:
    print("You are not 18 years old")

# Double Checks
if(name == "Gopal" and age == 18):
    print("Your name is Gopal and you are 18 years old")
else:
    print("Your name is not Gopal or you are not 18 years old")

if(name == "Gopal" or age == 18):
    print("Your name is Gopal or you are 18 years old")
else:
    print("Your name is not Gopal and you are not 18 years old")

# If-Elif-Else ladder
if(language == "Python"):
    print("print('Hello world')")
elif(language == "JavaScript"):
    print("console.log('Hello world')")
elif(language == "C++"):
    print('std::cout<<"Hello world";')
elif(language == "C"):
    print("printf('Hello world');")
else:
    print("Hello world")

# Ternary Operator
print("Your name is Gopal") if name == "Gopal" else print(f"Your name is {name}")

# Nested Conditionals
if(name == "Gopal"):
    if(age == 18):
        if(language == "Python"):
            print("Gopal is learning Python")
else:
    print("No one is learning.")

# Comparison Operators
if(age > 18):
    print("you are above 18 years old")
elif(age<18):
    print("you are below 18 years old")
elif(age>=18):
    print("you are 18 years old or above")
elif(age<=18):
    print("you are 18 years old or below")
elif(age==age1):
    print("you are 21 years old")
elif(age>90):
    print("you are above 90 years old")
elif(age<0):
    print("you are below 0 years old")
else:
    print("your age is unknown")

# Real Life example
if(user["token"]=="this is a very complex token"):
    if(user["age"]>18):
        if(user["role"] == "admin"):
            if(user["isLoggedIn"]):
                print("Allow")
            else:
                print("You Have to login first")
        else:
            print("You are not an admin")
    else:
        print("You are not allowed")
else:
    print("You are not authorised")

# Difference between is and ==
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print(a is b) # this will print false because is checks the identity of the object
print(a == b) # this will print true because == checks the value of the object

# False values
print(False)
print(bool(0))
print(bool(None))
print(bool(""))
print(bool({}))
print(bool(()))
print(bool([]))

# True values
print(True)
print(bool(1))
print(bool("Hello"))
print(bool([1,2,3]))
print(bool({"name":"Gopal"}))
print(bool((1,2,3)))