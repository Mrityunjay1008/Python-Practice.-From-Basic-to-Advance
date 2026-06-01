def route(rout):
    def decorator_function(fn):
        def wrapper(*args, **kwargs):
            print()
            print("Start of {}".format(fn.__name__))
            resutl = fn(*args, **kwargs)
            print("End of {}".format(fn.__name__))
            print()
            print(f"Routing to {rout}") 
            return resutl
        
        return wrapper

    return decorator_function


@route("/api/backend/user/profile?id=73269426")
def display_info(name,age):
    print("Display_info ran with arguments ({},{})".format(name,age))

display_info("Gopal",21)