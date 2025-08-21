print("This is my calculator\n")

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %, **): ")

if operator == "+":
    print(f"Result: {first_num + second_num}") 
elif operator == "-":
    print(f"Result: {first_num - second_num}")
elif operator == "*":
    print(f"Result: {first_num * second_num}")
elif operator == "/":
    print(f"Result: {first_num / second_num}")
elif operator == "**":
    print(f"Result: {first_num ** second_num}")
elif operator == "%":
    print(f"Result: {first_num % second_num}")
else:
    print(f"{operator} is not a valid operator")