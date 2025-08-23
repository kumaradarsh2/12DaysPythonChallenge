# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")
username_length = len(username)
contains_spaces = username.count(" ")
only_alpha = username.isalpha()

validation = "Valid user" if username_length <= 12 and not contains_spaces and only_alpha else "Invalid User"
print(validation)