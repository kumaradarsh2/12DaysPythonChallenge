# This is a comment about comment
print("I am excited to learn python")

# Variable: A resuable container for a value (String, Integer, Float, Boolean)

# String: Series of characters
first_name = "Adarsh"
last_name = "Kumar"

email = "adarshkr241@gmail.com"

print(f"{first_name} {last_name}")

print(f"My email is {email}")

#Integer: whole numbers
age = 21
quantity = 3 
num_of_students = 30

print(f"I am {age} years old")
print(f"I am buying {quantity} items")
print(f"My class has {num_of_students} students")

# Float: numbers (but contain decimal portion)
price = 9.99
gpa = 3.1
print(f"The price of pizza is {price}")
print(f"His gpa is: {gpa}")

# Boolean (true or false, they are binary)
has_won = True

if has_won: 
    print("He won")
else:
    print("He didn't win")


is_online = True

if is_online:
    print("You are online")
else:
    print("You are offline")

# Typecasting - It is the process of converting one data type to another
# following are the functions we use for typecasting
# str(), int(), float(), bool()

# we use type() function to get the type of specified object
name = "Adarsh Kumar"
age = 21
gpa = 3.4 
is_student = True

print(f"name is {type(name)} type\nage is {type(age)} type\ngpa is {type(gpa)} type\nis_student is {type(is_student)}")

# typecasting
# age = float(age)
age = str(age) # typecasted integer to string
age += "1" # string concatenation here
print(age)
print(type(age))

# let's try to typecast to bool
name = ""
name = bool(name)
print(name) # for non-empty string it gives true 

random_num = 0
random_num = bool(random_num)
print(random_num)

# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string 

user_name = input("What is your name?: ")
print(f"Hello {user_name}")

user_age = int(input("How old are you?: "))
user_age += 1
print(f"You are {user_age} years old")

# Arithmetic operator (+=, -=)
friends = 10

friends %= 3;

# friends **= 2

# friends /= 3
print(friends)

x = 3.14
y = -4
z = 5

# result = round(x) 
# result = abs(y) # to find the absolute value
result = pow(3,4) 
print(result)

max_value = max(x, y, z)
print(max_value)

min_value = min(x, y, z)
print(min_value)

# if statements

respose = input("Would you like some food (y/n): ")
if respose == "y":
    print("Have some food")
else:
    print("No food for you.")


# eg. 2
name = input("What's your name?: ")
if name == "":
    print("YOU DID NOT TYPE IN YOUR NAME!!")
else:
    print(f"Hello, {name}")


# use of boolean with if statement
for_sale = False
if for_sale:
    print("This item is for sale")
else:
    print("Not for sale")