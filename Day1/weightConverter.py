print("Weight converter")
print("Choose 'lb' or 'kg'")

from_unit = input("From: ")
to_unit = input("To: ")

weight = float(input("Enter weight: "))

if from_unit == "kg":
    # convert it to pounds
    converted_weight = weight * 2.20462262
else:
    # convert it to kg
    converted_weight = weight * 0.45359237

print(f"Weight in ({to_unit}): {round(converted_weight, 3)}")