principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break
    
while True:
    rate = float(input("Enter the Interest rate amount: "))
    if rate < 0:
        print("Interst rate can't be less than or equal to zero")
    else:
        break
    
while True:
    time = int(input("Enter the time amount: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break
    
amount = principle*((1 + rate/100)**time) 

print(f"Balance after {time} year is INR {amount: .2f}")