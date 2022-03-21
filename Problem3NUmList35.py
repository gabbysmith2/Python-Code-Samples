#Gabby Smith
#3.20.22
#Problem 3: Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100.
L= []

def sumlist(L):    
    sum = 0
    while sum <= 100:
        x = int(input("Enter a number:"))
        L.append(x)
        sum = sum + x
    return sum

print(sumlist(L))
print(L)
