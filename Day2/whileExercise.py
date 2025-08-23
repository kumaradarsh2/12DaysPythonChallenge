# Ask user for age, if age not valid then re-prompt them for age
age = input("Enter your age: ")

while age == "": 
    print("You didn't type your age")
    # re-prompt user for valid age (calling input function again)
    age = input("Enter your age: ")

print(f"You are {age if age.isdigit() else "INVALID"} years old")