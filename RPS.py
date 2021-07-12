import random

#This is a Rock, Paper, Scissor  prototype 
#basic principles such as variables, while -if -elif loops  , score increase apply 

choices = list(("Rock", "Paper", "Scissors"))
computer = random.choice(choices)
player = False 
computer_score = 0
player_score = 0

while True:
    player = input("Rock , Paper or Scissors :\n").capitalize()
    
    #Conditions of Choices (Rock,Paper,Scissors)

    if player == computer :
        print ("Tie!")

    elif player == "Rock":
        
      if computer == "Paper":
         
        print("You lose!",computer, "covers" , player)
        computer_score+= 1

      else :
          print("You win!",player, "smashes", computer)
          player_score+= 1
    
    elif player == "Paper":

      if computer == "Scissors":

        print("You lose!",computer, "cuts" , player) 
        computer_score+= 1

      else :
          print("You win!",player, "covers", computer)
          player_score+= 1
    

    elif player == "Scissors":
        
      if computer == "Rock":
         
        print("You lose!",computer, "smashes" , player)
        computer_score+= 1

      else :
          print("You win!",player, "cut", computer)
          player_score+= 1

    elif player == "End":
        
        print("Final Scores:")
        print(f"computer:{computer_score}")
        print(f"player{player_score}")
        break


    
    

