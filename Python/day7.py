#Some useful functions for day 7

#1. print()

#2. sum()
num1 = 10
num2 = 20
print(f"The sum of {num1} and {num2} is {sum([num1, num2])}")

#3. round()
num3 = 3.14159
print(f"The rounded value of {num3} is {round(num3)}")

#4. abs()
num4 = -15
print(f"The absolute value of {num4} is {abs(num4)}")

#5. area of a circle
import math
radius = 5
area = math.pi * radius ** 2
print(f"The area of a circle with radius {radius} is {area}")


#6. area of a circle
import math
diameter = 28
area = math.pi * diameter ** 2 / 4
print(f"The area of a circle with diameter {diameter} is {round(math.pi * diameter ** 2/4, 2)}")


#7. min & max 
num5 = float(input("Enter a number: "))
num6 = float(input("Enter a number: "))

print(f"The minimum of {num5} and {num6} is {min(num5, num6)}")
print(f"The maximum of {num5} and {num6} is {max(num5, num6)}")

print(f"The sum of {num5} and {num6} is {sum([int(num5), int(num6)])}")


#8. square of input number
num7 = float(input("Enter a number: "))
print(f"The square of {num7} is {math.pow(num7, 2)}")


