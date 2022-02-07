#Gabby Smith
#02.06.2022

#problem 1
#a program that prints hello world to the screen
print("Hello World")

#problem 2
#a program that asks the user for their name and greets them with their name
name=input("Enter your name: ")
print("Hello", name)

#problem 3
#program that only the users you and your instructor are greeted with their names
name=input("enter your name: ")
if name== "gabby" or name== "zoe":
    print("hello", name)

#problem 4
#program that computes the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer
print("Hello user, this program will computer the area of a circle")
pi=(3.14)
radius=input("Enter radius of your circle: ")
radius=float(radius)
area=pi*radius**2
print("Th area of your circle is", area, "thank you")

#problem 5
#program that computes MPG for a car
miles=input("how many miles?")
miles=float(miles)
gallons=input("how many gallons?")
gallons=int(gallons)
mpg=gallons//miles
print("Thank you! Your car has", mpg, "miles per gallon")

#problem 6
#converts fahrenheit to celsius
temp = input("Input the  temperature you like to convert?: ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")

#problem 7
#Calculate return day
start=int(input("From 0-6 what day is it?: "))
gone=int(input("How many days are you gone?: "))
end=(start+gone)%7
print("You will return on:", end)



