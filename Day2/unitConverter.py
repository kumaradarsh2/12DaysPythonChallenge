# goals is to make Unit converter which takes C, F, K

print("\n***************** This is unit converter program *****************\n")
print("Choose K (Kelvin), F (Fahrenheit) and C (Celsius) as units\n")

from_unit = input("Choose from unit: ")

has_lowercase = False

if from_unit.islower():
    has_lowercase = True
else:
    from_unit = from_unit.lower()

# check here
# if from_unit != "k" and from_unit != "f" and from_unit != "c":
if from_unit not in ("k", "f", "c"):
    if not has_lowercase:
        from_unit = from_unit.upper()
    print(f"{from_unit} is not valid unit")
    exit(1)

value = float(input("Enter value: "))
to_unit = input("Convert to unit:  ").lower()

# if to_unit != "k" and to_unit != "f" and to_unit != "c":
if to_unit not in ("k", "f", "c"):
    if not has_lowercase:
        from_unit = from_unit.upper()
    print(f"{from_unit} is not valid unit")
    exit(1)

if from_unit == "k":
    if to_unit == "f":
        converted = (value - 273.15) * 9/5 + 32
    else: 
        converted = value - 273.15
elif from_unit == "f":
    if to_unit == "c":
        converted = (value - 32) * 5 / 9
    else: 
        converted = (value - 32) * 5 / 9 + 273.15
else: 
    if to_unit == "k":
        converted = value + 273.15
    else: 
        converted = (value * 9/5) + 32

if not has_lowercase:
    to_unit = to_unit.upper()

print(f"{round(converted, 2)} {to_unit}")