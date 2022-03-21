#Gabby Smith
#3.20.22
#Problem 2: Using a while loop, create a list called L that contains the numbers 0 to 10. On each iteration, the loop should append the current value of a counter variable to the list and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.
def addlist(L):
    x = 0
    while x <= 10:
        L.append(x)
        x = x + 1
    return L

print(addlist(L))
