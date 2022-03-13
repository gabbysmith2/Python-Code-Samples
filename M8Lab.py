#Gabby Smith
#03.13.22
#P1: Function that takes two inputs from a user and prints whether they are equal or not
input1 = input("enter first input: ")
input2 = input("enter second input: ")
if(input1 == input2):
    print("They are equal.")
else:
    print("They are not equal.")

#P2: Function that takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10
def compare(x, y):
    z = x + y
    if z > 10:
        print("The sum is greater than 10.")
    elif z < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

compare(x, y)

#P3: a function that takes a list and prints if the value 5 is in that list
def list5(list):
    if 5 in list:
        print("5 is in this list")
    else:
        print("5 is not in this list")

list = [1, 2, 3, 4, 5]
list5(list)

list = [6, 7, 8, 9, 10, -5, 0]
list5(list)

#P4: a function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise
def leapyear(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year:"))
leapyear(year)
if leapyear(year) == True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
#P5: a function that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs. Confirm checks with print statements
#Task 1: Climb a mountain – needs rope, coat, and first aid kit, cannot have slow
def task1(items, debuffs):
    if "rope" and "coat" and "first aid kit" in items:
        if "slow" in debuffs:
            print("Character has correct items, but not correct status for Task 1: Climb a mountain")
        else:
            print("Character has correct items and status for Task 1: Climb a mountain")
    else:
        print("Character does not have correct items and status for Task 1: Climb a mountain")

#Task 2: Cook a meal – needs pan, groceries, cannot have small
def task2(items, debuffs):
    if "pan" and "groceries" in items:
        if "small" in debuffs:
            print("Character has correct items, but not correct status for Task 2: Cook a meal")
        else:
            print("Character has correct items and status for Task 2: Cook a meal")
    else:
        print("Character does not have correct items and status for Task 2: Cook a meal")

#Task 3: Write a book – needs pen, paper, idea, cannot have confusion
def task3(items, debuffs):
    if "pen" and "paper" and "idea" in items:
        if "confusion" in debuffs:
            print("Character has correct items, but not correct status for Task 3: Write a book")
        else:
            print("Character has correct items and status for Task 3: Write a book")
    else:
        print("Character does not have correct items and status for Task 3: Write a book")


items = ["pan", "paper", "idea", "rope", "groceries"]
debuffs = ["slow"]
task1(items, debuffs)
task2(items, debuffs)
task3(items, debuffs)
