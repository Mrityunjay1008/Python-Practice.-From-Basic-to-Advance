"""
LEGB
Local, enclosing, global, built-in
"""
import builtins

# Local and Global
x = "global X"

def test():
    y = "local Y"
    # x = "local X" # it will create a new x variable in this scope
    global x #This will change the global value of x but if you dont have any global variable x it will create a new global variable x **This is not used usually**
    x = "This is global X new value"
    print(y)
    print(x)

#print(y) it will throw error because y was intialised localy

def test1(z):
    print(z)

test()
test1("This is z")

# Builtins
m = min([5,1,2,3,4,5,0])
print(m)

# print(dir(builtins)) #This will show built in names

min = "hello" #You can use them as a variable etc but this is not recomended
print(min)

# Enclosing

def outter():
    x = 'outter x'
    def inner():
        nonlocal x # This will ignore the Local variable
        x = 'inner x'
        print(x) # This will always print "inner x" because it has a local variable x which has the value 'inner x'
    inner()
    print(x)  # This will always print "outter x" because it has a local variable x which has the value 'outter x'

outter()