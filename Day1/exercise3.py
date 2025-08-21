# calculate circumference of a circle
import math

# remove the multi-line comment to run the program
'''
radius = float(input("r: "))
circumference = 2 * math.pi * radius;
area = math.pi * pow(radius, 2);

# here's how we round it to a given decimal place
print(f"Circumference: {round(circumference, 2)} cm")
print(f"Area: {round(area, 2)} cc")

'''

# find hypotenuse of a right triangl
# formula: c = sqrt(a2 + b2)

perpendicular = int(input("a: "))
base = int(input("b: "))
hypotenuse = math.sqrt(perpendicular**2 + base**2)
print(f"h: {int(hypotenuse)}")