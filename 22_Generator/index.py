# Function
def square_the_given_array(nums):
    result = []
    for num in nums:
        result.append(num*num)

    return result

print(square_the_given_array([x for x in range(1,11)]))

# Generator
def square_the_given_array(nums):
    for num in nums:
        yield num*num
result =  square_the_given_array([x for x in range(1,11)])
print(next(result))
print(list(result))

# Generator Comprehension
result =  ((num**num)**(num**num) for num in [x for x in range(1,11)])
print(next(result))
print(list(result))