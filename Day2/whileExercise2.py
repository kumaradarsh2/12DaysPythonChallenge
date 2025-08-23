# ask user if they like to enter a food and q to quit
'''
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}, nice job")
    food = input("Enter a food you like (q to quit): ")
print("bye")
'''

# ask user to enter a number between 1 and 10
num = int(input("Enter number between 1 and 10: "))
while num < 1 or num > 10:
    print("That's not valid")
    num = int(input("Enter number between 1 and 10: "))
print("Congrats! You sucessfully typed number between 1 and 10")