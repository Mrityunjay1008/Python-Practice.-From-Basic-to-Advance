nums = ['a', 'b', 'c', 'd']

# For Loop
for num in nums:
    print(num)

# Break, Continue and Pass
# Break -> break the loop
# Continue -> continue the loop
# Pass -> do nothing

for i in range(5):
    if(i == 2):
        continue
    if(i == 4):
        break
    if(i == 3):
        pass
    print(i)

# Nested Loops 
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)

# While Loop
i = 0
while i < 5:
    print(i)
    i += 1 # if we don't do this, it will go on infinite loop

# Break, Continue and Pass also works
k = 0
while(True):
    if(k == 1000):
        break
    k+=100
    print(k)