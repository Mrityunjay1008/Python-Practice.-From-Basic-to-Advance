# Lists(These are mutable)
courses = ["history", "math", "physics", "chemistry"]
demi_course = ["physical education","music"]
nums = [1,2,3,4,5]

print(courses)
print(len(courses))
print(type(courses))

print(courses[0]) # index
print(courses[1:3]) # slicing
print(courses[-1]) # negative index
print(courses[0:4:2]) # step

# Lists Methods

courses.append("art")
courses.insert(2, "hindi")
courses.insert(0,demi_course)
courses.remove("art")
courses.reverse()
nums.sort(reverse=True)

print(nums)
print(courses.pop())
print(courses)
print(courses.index("physics"))

new_courses = courses.copy()
print(new_courses)

new_nums = sorted(nums)
print(nums)

print(sum(nums))
print(min(nums))
print(max(nums))

# Finding Index

print(courses.index("math"))

# Finding if the elem present

print("math" in courses)# return a boolean value

# Looping List

print("[",end=" ")
for course in courses:
    print(course, end=", ")
print("]")

for index,course in enumerate(courses):
    print(index,course)

# List to String

courses_string = ", ".join(courses)
print(courses_string)

# String to List

str1 = "This is a String"
string_list = str1.split(" ")
print(string_list)

# Tuples(These are immutable)

tuples = ("history", "math", "physics", "chemistry")
print(tuples)
print(len(tuples))
print(tuples[0])
print(tuples[0:3])
# tuples[0] = "social science" This will throw a error

# These are same as Lists BUT Tuples are immutable

# Sets (No Dublicate values are allowed)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

# Methods of sets
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))

# Creating Empty Lists, Tuples and sets

# List
empty_list = []
#or
empty_list = list()

# Tuple
empty_tuple = ()
#or
empty_tuple = tuple()

# Set
empty_set = set()
# not this
empty_set = {} # this will create a dictionary not set