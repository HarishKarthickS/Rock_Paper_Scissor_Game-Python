import random
#defining variable to store players score
Player_Score = 0

#defining variable to store computer score
Computer_Score = 0

#defining variable to store total number of round
round = 3

#defining list with the choices rock, paper, scissors
choices=[
		    "rock",
		    "paper",
		    "scissor"
]
#defining dictionary with the the winning combination
win={
   	     "rock":"scissor",
	     "paper":"rock",
  	     "scissor":"paper" 
}

#Using for loop to repeat the game for certain number of round
for i in range(0,round):

	#define a variable to store the input from the user
    player_choice = input("Enter your choice (rock, paper, scissor):")

 	#validate the players_choice
    if ( player_choice not in choices ):
	    print("Please enter a valid option")
	    continue

	#define a variable with a random choice for computer_choice
	
    computer_choice=random.choice(choices)

	#display players_choice and computer_choice
    print("Your choice :",player_choice,"\n Computer choice:",computer_choice)

	#display who won and update scores
    if ( player_choice == computer_choice ):
	    print("It's is a tie")
    elif ( win[player_choice] == computer_choice ):
	    print("Player win in this round")
	    Player_Score += 1
    else : 
	    print("Computer win this round")
	    Computer_Score += 1

	#display score of each round 
    print("\n Players Score :",Player_Score)
    print("\n Computer Score :",Computer_Score)

#Final result
if ( Player_Score > Computer_Score ) : 
	print("You win the Game, Congratulation")
elif ( Player_Score < Computer_Score ) : 
	print("The computer win the Game,Better Luck next time")
else : 
 	print( "The Game ends in draw" )
