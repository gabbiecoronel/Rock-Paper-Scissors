#Gabrielle Coronel
#COP 2500
#Final Project
#April 10, 2023

import random

print("Petey has challanged you to a game of rock paper scissors!\n")

#You chose rock as your weapon
def rock():
    print("Rock Paper Scissors Shoot!\n")
    #List's Petey's choice of weapons
    options=["Rock", "Paper", "Scissors"]
    #Randomizes Petey's choice of rock, paper, or scissors
    weapon=random.choice(options)
    petey=weapon
    #If Petey chose rock for his weapon
    if (petey=="Rock"):
        print("Your weapon: Rock", "VS Petey's weapon:", (petey))
        print("It's a tie\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")
    #If Petey chose scissors for his weapon
    elif (petey=="Scissors"):
        print("Your weapon: Rock", "VS Petey's weapon:", (petey))
        print("You won!\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")
    #If petey chose paper for his weapon
    else:
        print("Your weapon: Rock", "VS Petey's weapon:", (petey))
        print("You lost\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")

#You chose paper as your weapon
def paper():
    print("Rock Paper Scissors Shoot!\n")
    #List's Petey's choice of weapons
    options=["Rock", "Paper", "Scissors"]
    #Randomizes Petey's choice of rock, paper, or scissors
    weapon=random.choice(options)
    petey=weapon
    #If Petey chose paper for his weapon
    if (petey=="Paper"):
        print("Your weapon: Paper", "VS Petey's weapon:", (petey))
        print("It's a tie\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")
    #If Petey chose rock for his weapon
    elif (petey=="Rock"):
        print("Your weapon: Paper", "VS Petey's weapon:", (petey))
        print("You won!\n")
        print("Do you want to play again?")
        #Asks you to choose yes or no to play the game again
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")
    #If Petey chose scissors for his weapon
    else:
        print("Your weapon: Paper", "VS Petey's weapon:", (petey))
        print("You lost\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")

#You chose scissors as your weapon
def scissors():
    print("Rock Paper Scissors Shoot!\n")
    #List's Petey's choice of weapons
    options=["Rock", "Paper", "Scissors"]
    #Randomizes Petey's choice of rock, paper, or scissors
    weapon=random.choice(options)
    petey=weapon
    #If Petey chose scissors for his weapon
    if (petey=="Scissors"):
        print("Your weapon: Scissors", "VS Petey's weapon:", (petey))
        print("It's a tie\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")
    #If Petey chose rock for his weapon
    elif (petey=="Rock"):
        print("Your weapon: Scissors", "VS Petey's weapon:", (petey))
        print("You lost\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")
    #If Petey chose paper for his weapon
    else:
        print("Your weapon: Scissors", "VS Petey's weapon:", (petey))
        print("You won!\n")
        #Asks you to choose yes or no to play the game again
        print("Do you want to play again?")
        new_game=str(input("Yes or No\n"))
        #If you choose yes
        while(new_game=="Yes"):
            #Starts a new game
            return rock_paper_scissors()
        #If you chose no
        if (new_game=="No"):
            #Ends game
            print("Goodbye")

#Rock Paper Scissors Menu        
def rock_paper_scissors():
    #Your choice of weapons (rock, paper, or scissors)
    print("R - Rock")
    print("P - Paper")
    print("S - Scissors")
    you=input("Choose your weapon\n")
    #If you chose R
    if (you=="R"):
        #You chose rock as your weapon
        result=rock()
    #If you chose P
    elif (you=="P"):
        #You chose paper as your weapon
        result=paper()
    #If you chose S
    elif (you=="S"):
        #You chose scissors as your weapon
        result=scissors()
    #If you chose something else other than R, P, or S
    else:
        print("That's not an option\n")
        #Brings you back to your choice of weapons
        result=rock_paper_scissors()
        
rock_paper_scissors()
    
    
