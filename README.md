# Rock_Paper_Scissor_Game-Python-
Rock, paper, scissor

# Game description :
Rock ,paper,scissor is an intransitive hand game,usually played between two people,in which each player simultaneously forms one one of the three shapes using the hand.

# Rules :
Rock, Paper, Scissor is a popular game that is played by two or more players.The players simultaneously choose one of the three option:
-Rock
-Paper
-Scissor
The winner is decided by following these rules :
-Rock beats scissor, because the rock smashes the scissor.
-Paper beats the rock, because paper covers the rock.
-Scissor beats the paper, because the scissor cuts the paper.

# Pseudocode :

	#defining variable to store players score
	Let Player_Score = 0

	#defining variable to store computer score
	Let Computer_Score = 0

	#defining variable to store total number of round
	Let round = 3

	#defining list with the choices rock, paper, scissors
	Let choices={
		    “rock”,
		    “paper”,
		    “scissor”
	}
	#defining dictionary with the the winning combination
	Let win={
   	     “rock”:”scissor”,
	     “paper”:”rock”,
  	     “scissor”:”paper” 
	}

	#Using for loop to repeat the game for certain number of round
	for i in range(0,round):

		#define a variable to store the input from the user
		Let player_choice = input(“Enter your choice (Rock, Paper, Scissor):”)

 		#validate the players_choice
		If (player_choice not in choices):
			print(“Please enter a valid option”)
			continue

		#define a variable with a random choice for computer_choice
		Let computer_choice = random.choice(choices)

		#display players_choice and computer_choice
		print(“Your choice :”,player_choice,”Computer choice:”,computer_choice)

		#display who won and update scores
		if ( player_choice == computer_choice ):
			print(“It’s is a tie”)
		else if ( win[player_choice] == computer_choice ):
			print(“Player win in this round”)
			Player_Score += 1
		else : 
			print(“Computer win this round”)
			Computer_Score += 1

		#display score of each round 
		print(“\n Players Score :”,Player_Score)
		print(“\n Computer Score”,Computer_Score)

	#Final result
	If ( Player_Score > Computer_Score ) : 
		print(“You win the Game, Congratulation”)
	else if ( Player_Score < Computer_Score ) : 
		print(“The computer win the Game,Better Luck next time”)
	else : 
 		print( “The Game ends in draw” )

		


