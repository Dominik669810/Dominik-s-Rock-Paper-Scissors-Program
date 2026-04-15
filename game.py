import random # Imports a rand py library for the program to choose a random option out of the list choices
import os 

def draw(choice):
    if choice == "rock":
    # Player chose rock, so rock symbol 
     return("""
        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
           
          """ )
    
    elif choice == "paper":
    # Player chose paper
     return("""
    _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)

     
           """ )
    elif choice == "scissors":
    # Player chose scissors
     return("""
            
            
   _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
            
            
            """)
      


choices = ["rock", "paper", "scissors"] # Uses a list to hold the three main choices

def determine_winner(player, opp): # Uses a function to determine the games overall winner
   # Tie
   if player == opp:
      print("It is a tie!")

    # Player won

   elif (( player == "rock" and opp == "scissors" ) or 
          ( player == "paper" and opp == "rock" ) or
          ( player == "scissors" and opp == "paper")):
             return("You won the game!")
   # Computer won
   else:
       return("You lost, sorry")
   
playing, invalid = True, False 

while playing:
    # Player makes a selection
    # Checks whether player selection is valid or invalid and informs the player
    if not invalid:
      print("Please choose either rock, paper, or scissors.")
    else:
      print("Invalid input, please choose either rock, paper or scissors.")
      invalid = False
      print("Or enter q to quit.")


    player_choice = input().lower().strip() # Reviews the players input, .lower automatically applies lowercase to all input, and .strip removes whitespace
    
    opp_choice = random.choice(choices) # The computer chooses a random choice from the list "choices"

    if player_choice in choices:
        print(f"You chose {player_choice} {draw(player_choice)}.")
        print(f"The opponent has chosen {opp_choice} {draw(opp_choice)}.")
        print(determine_winner(player_choice, opp_choice))

    elif player_choice == 'q': # If the player presses q, the while loop breaks, and the program ends
        playing = False
        print("You have closed the program.")

    else:
        invalid = True
    # Asking user to play again:
    if playing and not invalid:
       replay = input("Do you want to play again? \nType \"yes\ to replay, or\n enter aything else to end the game.\n").lower().strip()
       print()
       playing = replay == "yes" 

       # Clears the screen

       os.system('cls' if os.name == 'nt' else 'clear')


print("Thank you for playing!")
