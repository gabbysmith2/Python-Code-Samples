#Chapter 1 Intro
def chapter5():
    print("The player walks a further distance, and shortly comes to a group of mutants having a shooting battle with a small group of survivors.")
    answer=input("Greetings sole survivor! Are you ready to play? (yes/no) ")
    if answer.lower().strip()=="yes":

        answer=input("A group of large green radiation poisoned mutants are at war with humans. (join the fight/exit) ")
        if answer=="join the fight":
            print("You bravely defreat the mutants and protect the village...for now. Good game!")
        
        elif answer=="exit":
            answer==input("You realize you are outnumbered and return to the small settlement for more supplies.")

        else:
            print("Invalid input. Please try again!")
    else:
        print("That's too bad!")

def chapter4():
    print("The vault opens. The player examines the wasteland. Battered buildings, bridges completely collapsed, and no sign of any other survivor.")
    answer=input("Welcome to chapter 2. Are you ready to play? (yes/no) ")
    if answer.lower().strip()=="yes":

        answer=input("Player comes across and small settlement after miles of walking. They are friendly farmers, who warn of a mutant colony in the distance who have been stealing from them. You may interact, take on tasks, stay, or travel to take on the mutants. ")
        if answer=="interact":
            print("You make a quick stop at teh village to talk to settlers to get more information. They tell you the mutants have been stealing what little food they have for weeks. You agree to take up the fight for the starving villagers. Proceed to Chapter 4 when ready")
        
        elif answer=="take on tasks" or "stay":
            answer==input("You stay at the village to refuel and get money and supplies for your fight with the mutants. Proceed to chapter 5 when ready.")
            chapter5()

        elif answer=="take on the mutants":
            print(chapter5())

        else:
            print("Invalid input, please try again")
    else:
        print("That's too bad!")

def chapter3():
    print("Through the next door. You are hit with a strange smell. You have discovered the opening to the vault. ")
    answer=input("Welcome to chapter 2. Are you ready to play? (yes/no) ")
    if answer.lower().strip()=="yes":

        answer=input("There is bright light peaking through the doors. Brace yourself for what is to come. Would you like to stay or exit? ")
        if answer=="stay":
            print("You pause at the vault door to contemplate. Proceed to Chapter 4 when ready")
        
        elif answer=="exit":
            answer==input(chapter4())

        else:
            print("Invalid input, please try again")
    else:
        print("That's too bad!")
def chapter2():
    print("The door opens into a hallway infested with radroaches. The only way is through.")
    answer=input("Welcome to chapter 2. Are you ready to play? (yes/no) ")
    if answer.lower().strip()=="yes":

        answer=input("There is a lockbox on the right wall containing a gun and ammo, as well as healing aides. How do you proceed? open lockbox, attack roaches, muscle through")
        if answer=="open lockbox":
            print("You have found a pistol, you may move on to chapter 3")
        
        elif answer=="attack roaches":
            answer==input("The roaches hurt you, but you win out in the end. Move on to Chapter 3")

        else:
            print(chapter3())
    else:
        print("That's too bad!")

def chapter1():
    print("It is eerily quiet. The bombs fell 10 years ago, and the player has finally woken up from her cryogenic chamber and is making her way through the underground vault. She is the only survivor.")
    answer=input("Greetings sole survivor! Are you ready to play? (yes/no) ")
    if answer.lower().strip()=="yes":

        answer=input("It is dark, she only has on her her vault suit. The vault is cold, and the only sign of life are radiation poisoned giant roaches. Would you like to look for power switch, search for tools, or exit the cryogenic chamber room?")
        if answer=="look for power switch":
            print("the lights are now on, you may move on to chapter 2")
        
        elif answer=="search for tools":
            answer==input("You have found a knife, you may move on to chapter 2")

        elif answer=="exit the cryogenic chamber room":
            answer==input(chapter2())

        else:
            print("Invalid input. Please try again!")
    else:
        print("That's too bad!")
chapter1()

