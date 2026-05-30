# Lists

unsorted_list = [1,65,24,56,8,53,463,5,7,4,3,33,44,77,]

sorted_list = sorted(unsorted_list)

# sorted(unsorted_list) != unsorted_list.sort()
# sorted method returns a new list where as sort method returns None but sorts the originallist

reversed_sorted_list = sorted(unsorted_list, reverse=True)

print(f"Unsorted List: {unsorted_list}")
print(f"Sorted List: {sorted_list}")
print(f"Reversed Sorted List: {reversed_sorted_list}")

# Tuples

unsorted_tuple = (1,65,24,56,8,53,463,5,7,4,3,33,44,77,)

unsorted_list.sort()

print(f"Unsorted Tuple: {unsorted_list}")

sorted_tuple = sorted(unsorted_tuple)

print(f"Unsorted Tuple: {unsorted_tuple}")
print(f"Sorted Tuple: {sorted_tuple}")

# Sets

unsorted_set = {1,65,24,56,8,53,463,5,7,4,3,33,44,77,}

sorted_set = sorted(unsorted_set)

print(f"Unsorted Set: {unsorted_set}")
print(f"Sorted Set: {sorted_set}")

# Absolute Value

li = [-6,-5,-4,1,2,3]

abs_list = sorted(li, key=abs)

print(f"Unsorted List: {li}")
print(f"Sorted List: {abs_list}")

# Employees

e1 = {"name": "John", "age": 30, "salary": 50000}
e2 = {"name": "Jane", "age": 25, "salary": 60000}
e3 = {"name": "Bob", "age": 35, "salary": 70000}

employees = [e1,e2,e3]

sorted_employees = sorted(employees, key= lambda x: x["age"])

print(f"Unsorted List: {employees}")
print(f"Sorted List: {sorted_employees}")

