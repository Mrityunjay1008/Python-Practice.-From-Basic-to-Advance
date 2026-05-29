# variable should be descriptive 
# stringe should be in double or single quotes
my_message = "Hello world"
your_message = 'Hello world'
gopal_message = """Hello world"""
god_message = '''Hello world'''
human_message = "human's Message"

print(my_message)
print(your_message)
print(gopal_message)
print(god_message)
print(human_message)

print(len(my_message))

# print(my_message[index]) this will print the char at index
# range of index = [0,len(my_message)-1]

print(my_message[0])

# it will print my_message[0] to my_message[4]
print(my_message[0:5])

print(my_message[6:11])

# Some Methods of string
print(my_message.upper())
print(my_message.lower())
print(my_message.title())
print(my_message.count('l'))
print(my_message.find('l'))
print(my_message.find('Hello'))
print(my_message.find('world'))
print(my_message.replace('Hello', 'Hi'))#it wont change the original string

# concat
print(my_message + ' ' + human_message + '. Welcome to python')

# f string formated string
print(f'Your message is {my_message}')
message2 = '{} {} This is the second message'.format(my_message, human_message)
print(message2)

# For reference And Learning
print(dir(my_message))
print(help(str)) #This doesnt work on variable
print(help(str.len)) #For specific method