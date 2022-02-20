#Gabrielle Smith, 2.20.2022
#problem 1 prints hello world to the screen 100 times
for numbers in range(100):
    print("Hello World")
#problem 2
n = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for numbers in n:
    print(numbers)

for numbers in n:
    print(numbers, numbers**2)
#problem 3
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

sides = eval(input("Number of sides?" ))
length = eval(input("Length of the side?" ))
colorname = eval(input("Color of the line?" ))
fcolor = eval(input("Fill color?" ))

alex.color = (colorname)
alex.fillcolor = (fcolor)

for i in range(int(sides)):
    alex.forward(int(length))
    alex.left(int(360) / int(sides))

#problem 4
for divisibles in range(51):
    if divisibles % 3==0 and divisibles % 5==0:
        print("Divisible by both")
        continue
    elif divisibles % 3==0:
        print("divisible by three")
        continue
    elif divisibles % 5==0:
        print("divisible by five")
        continue
    print(divisibles)
#problem 5 draw a picture
import turtle    
trtl = turtle.Turtle()    
screen=turtle.Screen()   
screen.setup(400,300)    
screen.bgcolor('black')    
trtl.pencolor('red')   
trtl.pensize(5)    
trtl.speed(1)    
trtl.shape('turtle')   
for i in range(4): 
      trtl.forward(100)  
      trtl.right(90)    

