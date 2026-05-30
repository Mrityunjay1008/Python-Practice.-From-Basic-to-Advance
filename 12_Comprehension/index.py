# List Comprehension

natural_list = [1,2,3,4,5,6,7,8,9,10]

list_num = [x for x in natural_list]
print(list_num)

list_sq = [x**2 for x in natural_list]
print(list_sq)

list_cube = [x**3 for x in natural_list]
print(list_cube)

list_nN = [x**x for x in natural_list]
print(list_nN)

list_nNn = [(x**x)*x for x in natural_list]
print(list_nNn)

list_even = [x for x in natural_list if x%2==0]
print(list_even)

list_odd = [x for x in natural_list if x%2!=0]
print(list_odd)

list_letter_num = [(letter,num) for letter in "abc" for num in range(1,4)]
print(list_letter_num)

# Dictionary Comprehension

names = ["tony stark","natasha","gangadhar"]
heroes = ['iron man','black widow','shaktimaan']

heroes_dict = {names:hero for names, hero in zip(names,heroes)}
print(heroes_dict)

# Set Comprehension

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set3 = {x for x in set1 if x in set2}
print(set3)

set4 = {x for x in set1 if x not in set2}
print(set4)

set5 = {x for x in set1 if x%2==0}
print(set5)

set6 = {x for x in set1 if x%2!=0}
print(set6)

# Generator Comprehension

my_gen = (n*n for n in natural_list)
for i in my_gen:
    print(i)