# Zhusupova Sezimgul
# 10/17/2026
# Calculation program
import math
# All solutions for all problems are in one file, so uncomment each function to run separately


 #Problem 1
print("Hello World")

# Problem 2 and 3 ----------------------------------------------------------------------
username = input("Enter your name: ")
if username == "Sezimgul" or username == "Antonio":
     print("Hello", username, "!")
else:
     print("Sorry, the program greets only Sezimgul and the professor")

# Problem 4 -------------------------------------------------------------------------------
# import math
#
radius = float(input("enter the radius"))
area = math.pi * radius ** 2
print("the area of the circle is", area)

# problem 5---------------------------------------------------------------------------------
mile = float(input("Enter the number of miles driven"))
gallons = float(input("Enter the number of gallons used"))
#
mpg = mile / gallons
print("Result:", mpg)

# Problem 6----------------------------------------------------------------------------------
fahrenheit = float(input("Enter the fahrenheit temperature: "))
celsius = (5 / 9) * (fahrenheit - 32)
print(celsius)

# Problem 7----------------------------------------------------------------------------
day_start = int(input("Start day in number (0-6):"))
length = int(input("Amount of nights:"))
#
return_day = (day_start + length) % 7
result = 0
if return_day == 0:
    result = "Sunday"
elif return_day == 1:
     result = "Monday"
elif return_day == 2:
     result = "Tuesday"
elif return_day == 3:
     result = "Wednesday"
elif return_day == 4:
     result = "Thursday"
elif return_day == 5:
     result = "Friday"
elif return_day == 6:
     result = "Saturday"
#
print("Your will be back in", result)
