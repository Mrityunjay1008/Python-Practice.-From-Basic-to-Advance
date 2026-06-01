try: # This is a try block
    f = open("20_Try_Except/text_code.txt","r")
    if(True):
        raise Exception("This is a manual error") # This will raise an error

except FileNotFoundError as e: # This is a except block if the file is not found
    print(e)

except Exception as err: # This is a except block if the error is generic
    print(err)

else: # This will run if there is no error
    print(f.read())

finally: # This will run no matter what
    print("File is closed")
    f.close()