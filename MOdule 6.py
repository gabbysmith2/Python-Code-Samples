#Gabby Smith
#2.27.2#2.27.2022

#Problem 1
#Use a for statement and random.randrange to print 10 random integers between 25 and 35
import random
print(random.sample(range(25,35),10))

#Problem 2
#Use random.randrange to print an odd integer between 0 and 100.
print (random.randrange(1, 100, 2))

#Problem 3
#Use random.choice to select a day of the week from a list and print that day
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
print(random.choice(days))

#problem 4
#Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.
import math
print(math.pi)

from math import acos
def printValueofpi():
    pi=round(2*acos(0.0),3)
    print(pi)
