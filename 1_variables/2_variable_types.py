# Data Types
# There are many different data types
# 1. int: integer (1, 2, -1, ...)
# 2. float: floating point (3.14, 1.23456, ...)
# 3. str: string - a sequence of characters 'Hello' "Hello"
# 4. bool: boolean (True, False)
# 5. list: ....
# ...

language = "en_us"
print(type(language))

users = 10
print(type(users))

print(str(users) + language)  # "10" + "en_us" => "10en_us"

# Type Conversion (type casting) : changing types
# There are several built-in functions that let you convert one data type to another.
#
# str(x): converts x to a string
# int(x): converts x to an integer
# float(x): converts x to a floating point number

y = "12"
z = int(y)
print(z + 10)

a = "3.14"
b = float(a)
print(type(b))

# Exercise: what is the type of the following operations?
# 1. 10 / 2 -> float
print(type(10 / 2))

# 2. 10 // 2 -> int
print(type(10 // 2))

# 3. float(5) -> 5.0 float
print(float(5))
print(type(float(5)))
