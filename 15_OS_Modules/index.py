import os # King of all modules
import datetime

# print(dir(os)) This will how many methods are available

print()
print(os.name) #This will print the name of the operating system

print()
print(os.getcwd()) #This will print the current working directory

print()
print(os.listdir()) #This will print the list of files and directories in the current working directory

# print()
# print(os.environ) #This will print the environment variables

print()
print(os.path.abspath(__file__)) #This will print the absolute path of the current file 

print()
print(os.path.dirname(os.path.abspath(__file__))) #This will print the directory name of the current file

print()
os.mkdir("new_folder") #This will create a new folder in the current working directory
os.rmdir("new_folder") #This will remove a folder in the current working directory

# os.mkdir("15_OS_Modules/new_folder") #This will create a new folder in the current working directory
# os.rmdir("15_OS_Modules/new_folder") #This will remove a folder in the current working directory

print(os.stat("15_OS_Modules/index.py")) # This will print the statistics of the current file

print()
print(os.path.getsize("15_OS_Modules/index.py")) # This will print the size of the current file in bytes

print()
last_modified_time = os.stat("15_OS_Modules/index.py").st_mtime # This will print the last modified time of the current file
print(datetime.datetime.fromtimestamp(last_modified_time))

print()
for dirpath, dirnames, filenames in os.walk(os.getcwd()): #This will print the list of files and directories in the current working directory
    print("Current path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)

print()
print(os.path.exists("15_OS_Modules/index.py")) #This will return True if the file exists and False if it doesn't

print()
print(os.path.basename(os.path.abspath(__file__))) #This will print the base name of the current file

print()
print(os.path.splitext(os.path.basename(os.path.abspath(__file__)))) #This will print the base name and extension of the current file