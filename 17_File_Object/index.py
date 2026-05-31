f = open("17_File_Object/test.txt","r")
print(f.read())
f.close()

with open("17_File_Object/test.txt","r") as f: # This will close the file automatically
    print(f.read())

print(f.closed)

with open("17_File_Object/test1.txt","r") as f: # This will close the file automatically
    exec(f.read())

for line in open("17_File_Object/test.txt","r"):
    print(line)

with open("17_File_Object/test1.txt","r") as f:
    for line in f:
        print(line)

with open("17_File_Object/test2.txt","r") as f:
    size_to_read = 100
    f_content = f.read(size_to_read)
    f.seek(0)
    print(f.tell())
    while len(f_content) > 0:
        print(f_content)
        f_content = f.read(size_to_read)

# Writing to a file
with open("17_File_Object/test3.txt","w") as f:
    f.write("This is writing to a file")
    f.seek(0)
    f.write("For")

with open("17_File_Object/test1.txt","r") as f:
    with open("17_File_Object/test4.txt","w") as f1:
        for line in f:
            f1.write(line)

# Appending to a file
with open("17_File_Object/test1.txt","a") as f:
    f.write("\nThis is appending to a file")