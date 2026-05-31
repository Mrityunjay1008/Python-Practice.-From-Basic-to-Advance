import random

greetings = ["Ram Ram", "Shyam Shyam","Radhe Radhe","Krishna Krishna","Namaste"]
vibgyor = ["Vibgyor","Indigo","Blue","Green","Yellow","Orange","Red"]
deck = list(range(1,53))

value = random.random() # random float number between 0 and 1
print(value)

value1 = random.randint(1,10)
print(value1)

value2 = random.choice(greetings)
print(value2+"! Gopal")

value3 = random.choices(vibgyor,k=3)
print(value3)

random.shuffle(deck)
print(deck)

value4 = random.sample(deck,k=5)
print(value4)