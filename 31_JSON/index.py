import json

# data = json.loads(user)
# print(type(data),data)

# We are gonna see real life example

with open("31_JSON/users.json","r") as f:
    data = json.load(f)
    
def user_creation_decorator(fn):
    def wrapper(given_user):
        for user in data["users"]:
            if given_user["email"] == user["email"]:
                raise Exception("Email already exists")
            if given_user["name"] == user["name"]:
                raise Exception("Name already exists")

        return fn(given_user)
    return wrapper

@user_creation_decorator
def create_user(user):

    new_user = {
        "id": len(data["users"]) + 1,
        "name":user["name"],
        "email":user["email"],
        "password":user["password"],
        "isLoggedIn": True,
        "age": user["age"],
        "isActive": True
    }
    
    data["users"].append(new_user)
    with open("31_JSON/users.json","w") as f:
        json.dump(data,f,indent=4)
    return {"success":True,"message":"User created successfully","user":new_user}

def login_user(email,password):
    for user in data["users"]:
        if user["email"] == email and user["password"] == password:
            user["isLoggedIn"] = True
            with open("31_JSON/users.json","w") as f:
                json.dump(data,f,indent=4)
            return {"success":True,"message":"User logged in successfully","user":user}
        
    return {"success":False,"message":"User not found","user":None}

def logout_user(email,password):
    for user in data["users"]:
        if user["email"] == email and user["password"] == password:
            user["isLoggedIn"] = False
            with open("31_JSON/users.json","w") as f:
                json.dump(data,f,indent=4)
            return {"success":True,"message":"User logged out successfully","user":user}
        
    return {"success":False,"message":"User not found","user":None}

isLoggedIn = input("Are you logged in(Y/N): ")

if(isLoggedIn == "Y" or isLoggedIn == "y"):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    res = login_user(email,password)
    if(res["success"]==False):
        print(res["message"])
        exit()
    print(f'\n{res["user"]}\n')
elif(isLoggedIn == "N" or isLoggedIn == "n"):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    age = int(input("Enter your age: "))
    try:
        res = create_user({"name":name,"email":email,"password":password,"age":age})
        print(f'\n{res["user"]}\n')
    except Exception as e:
        print(e)
        exit()
else:
    print("Invalid input")
    exit()