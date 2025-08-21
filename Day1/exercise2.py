item = input("What item would you like to purchase: ")
price = float(input("What's the price?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity
print(f"You have bought {quantity} x {item}")
print(f"You total is INR {total}")