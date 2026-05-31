import datetime

user = {
    "name":"Gopal",
    "age":21,
    "email":"j5AeQ@example.com",
    "isLoggedIn":True
}

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

print()
print(f"Name: {user['name']}\nAge: {user['age']}\nEmail: {user['email']}\nIs Logged In: {user['isLoggedIn']}")

print()
print("Name: {}\nAge: {}\nEmail: {}\nIs Logged In: {}".format(user['name'],user['age'],user['email'],user['isLoggedIn']))

print()
print("<{0}>{1}</{0}>".format("h1","This is a h1 tag"))

print()
print("Name:{0[name]}\nAge:{0[age]}\nEmail:{0[email]}\nIs Logged In:{0[isLoggedIn]}".format(user))

print()
print("Name:{name}\nAge:{age}\nEmail:{email}\nIs Logged In:{isLoggedIn}".format(name="Gopal",age=21,email="j5AeQ@example.com",isLoggedIn=True))

print()
print("Name:{name}\nAge:{age}\nEmail:{email}\nIs Logged In:{isLoggedIn}".format(**user))

print()
print("Pi Value: {}".format(pi))

print()
print("Pi Value: {:.2f}".format(pi))

print()
print("1MB is equal to {:,.2f} bytes".format(1024*1024))

print()
my_date = datetime.datetime.now()
print("{:%B %D, %Y}".format(my_date))

print()
print("{0:%B %D, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date))