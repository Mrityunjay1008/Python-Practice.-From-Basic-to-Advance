int1 = 10
int2 = 20

# Basic Arithmetic

print(int1 + int2)  # addition  30
print(int1 - int2)  # subtraction -10
print(int1 * int2)  # multiplication 200
print(int1 / int2)  # float 0.5
print(int1 % int2)  # modulus(remainder) 10
print(int1 ** int2)  # power 100000000000000000000
print(int1 // int2)  # floor division 0

# Order of operations
# PEMDAS
# Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction

print(10 + 20 * 30) #610
print((10 + 20) * 30) # 900

# Methods
print(int1.__add__(int2))
print(int1.__sub__(int2))
print(int1.__mul__(int2))
print(int1.__truediv__(int2))
print(int1.__mod__(int2))
print(int1.__pow__(int2))
print(int1.__floordiv__(int2))

print(round(3.4))
print(abs(-3.4))
print(int(3.4))
print(float(3))

num1 = 3
num2 = 2

# Comparison Operators
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# Type Conversion
num3 = "10"
num4 = "20"

num3 = int(num3)
num4 = int(num4)

print(num3 + num4)

# Multiple Assignment
num1, num2, num3 = 10, 20, 30

# Assignment Operators
num1 += 10
num1 -= 10
num1 *= 10
num1 /= 10

# Arithmetic with Strings
str1 = "Hello"
str2 = "World"
num5 = 10

print(str1 + str2)
print(str1 * num5)