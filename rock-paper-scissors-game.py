def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        pass
    return number
#changes name into number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        pass
    return name
#changes number to name
        
def rpsls(player_choice):
    import random
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    #generates computer choice
    print("Player chooses", player_choice)
    print("Computer chooses", comp_choice)
    #prints choices of player and computer
    player_number = name_to_number(player_choice.lower())
    if comp_choice == player_choice:
        print("Draw!")
    elif comp_choice == "rock":
        if player_number == (3 or 4):
            print("Computer Wins")
        else:
            print("Player Wins")
              
    elif comp_choice == "scissors":
        if player_number == (2 or 3):
            print("Computer Wins")
        else:
            print("Player Wins")
              
    elif comp_choice == "lizard":
        if player_number == (1 or 2):
            print("Computer Wins")
        else:
            print("Player Wins")
              
    elif comp_choice == "paper":
        if player_number == (0 or 1):
            print("Computer Wins")
        else:
            print("Player Wins")
            
    elif comp_choice == "spock":
        if player_number == (0 or 4):
            print("Computer Wins")
        else:
            print("Player Wins")
    else:
        pass
    #Determines winner
    print()
    #creates space between games
    
    
    

    
rpsls(input("enter choice"))
#runs function with user input
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#runs function
