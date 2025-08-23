# logical operator = evaluate multiple conditions (or, and, not)

#                    or => at least one of the condition 
#                    and => both conditions must be true  
#                    not => inverts the condition (not False, not True)

# Note: we can link "logical operators" together

'''
temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 0 < temp < 28 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY 🌞")
elif temp >= 28 and not is_sunny:
    print("It is HOT ouside")
    print("It is CLOUDY ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁️")
else:
    print("Come'on let's go play outside :)")
'''

# conditional expression (ternary operator)
# (return) X if codition else (return) Y

num = 5
a = 6 
b = 7
age = 17
temperature = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# max_num = a if a > b else b;
# min_num = a if a < b else b;
# print(min_num)
# check if number is even or odd
# print("Even" if num % 2 == 0 else "Odd")
#status = "Adult" if age >= 18 else "Child"
#weather = "Hot" if temperature > 35 else "Cold"
# full_access = "Full Access" if user_role == "admin" else "Limited Access"
#print(full_access)

name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# String is just the series of characters
# get length of string using len(): includes spaces too

# .find() method: returns first occurrence of a given character
# .rfind() method: returns last occurrence of a given character
#  Note: both above method return -1 if character is not found

# .capitalize() method: this capitalizes first character in a string
# .upper() method: This makes every character uppercase 
# .lower() method: This makes every character lowercase 
# .isdigit() method: returns true if the string contains only digits (not even alphanumeric) 
# .isalpha() method: returns true if string contains only alphabet
# .count("<character_here>"): returns number of character in string 
# .replace("<jisko_replace_krna_h>, <jisse_replace_krna_h>")

# phone_number = phone_number.replace("-", "")
# print(phone_number)

# help() gives comprehensive list of string method available
# result = help(str)
# print(result)

# indexing = accessing elements of a sequence using [] (indexing operator) [start : end : step]
# start is inclusive and end is exclusive
credit_number = "1234-5678-9012-3456"

# print(credit_number[0 : 4])
# print(credit_number[ : 4])

# print(credit_number[5 : 9])
# print(credit_number[5 : 9])

# last 12 digits
# print(credit_number[5 : ])

#using negative index we start from last (starting from -1)
# print(credit_number[-1])

# using [ : : <steps_to_skip_here>]
# get last 4 digit of credit_number

last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# to reverse a string, we set "step" to be -1
reversed_credit_number = credit_number[ : : -1]
# print(reversed_credit_number)

# format specifier
price1 = 3.141592
price2 = -784.80
price3 = 12.34

# print(f"Price 1 is {price1 : .3f}")
# print(f"Price 2 is {price2 : .3f}")
# print(f"Price 3 is {price3 : .3f}")

# while loop

while name == "":
    name = input("Enter your full name: ")
print(f"Hello {name}")