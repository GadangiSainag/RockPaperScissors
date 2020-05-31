import random


while True:
	choices=['Rock','Paper','Scicors']


	matches=0
	tied=0
	player=0
	computer=0
	shit=['HELP','ROCK','PAPER','SCICORS']

	hard_rock=['Paper','Scicors','Paper','Scicors','Paper']#defeat
	hard_paper=['Scicors','Rock','Scicors','Rock','Scicors']
	hard_scicors=['Rock','Paper','Rock','Paper','Rock']

	print("WELCOME TO THE BEST GAME OF ROCK,PAPER AND SCICORS")
	print("\n\nSelect your mode (1.NORMAL MODE  2.HARD MODE   3.EXTERME MODE)")

	mode=input().strip()
	print("\n\n")
	normal=False
	extreme=False
	hard=False

	try :
		mode=int(mode)
	except ValueError:
		print("\nerror :i can't understand you\nAs always mode is set to NORMAL")
		normal=True
	

	if type(mode)==int:
		if mode==3:
			extreme=True
			print("YOU CHOOSE EXTREME MODE\nI BET YOU CAN'T WIN THIS......")

		elif mode==1:
			normal=True
			print("You have chosen NORMAL mode\nGOOD LUCK")

		elif mode==2:
			hard=True
			print("You Choose HARD mode..\n TRY HARD FOR THE WIN\n")
		
		elif mode not in (1,2,3):
			print("I can't understand you......\nAs always mode is set to NORMAL")
			normal=True
			


	#--------------------FUNCTIONS---------------#
	def quit(matches,player,computer,tied):
		print("\n")
		print("|-----------RESULTS---------|")
		print("Total matches: ", matches)
		print("Your score:",player)
		print("Computer score:",computer)
		print("Tied: ",tied,"\n\n")
		
		if player>computer:
			print("|--------------------|")
			print("| Overall PLAYER won |")
			print("|--------------------|\n\n")

		elif player==computer:
			print("|-----------------------------------|")
			print("| Both the COMPUTER and PLAYER tied |")
			print("|-----------------------------------|\n\n")

		else:
			print("|----------------------|")
			print("| Overall COMPUTER won |")
			print("|----------------------|\n\n")


	def winner(user_choice,computer_choice):
		global matches, player, computer, tied, choices
		if user_choice==1:
			matches+=1
			if computer_choice==choices[0]:
				print("Tied")
				tied+=1
			elif computer_choice==choices[1]:
				print("The computer won")
				computer+=1
			else :
				print("You won")
				player+=1
		
		elif user_choice==2:
			matches+=1
			if computer_choice==choices[0]:
				print("You won")
				player+=1
			elif computer_choice==choices[1]:
				print("Tied")
				tied+=1			
			else :
				print("The computer won")
				computer+=1
		
		elif user_choice==3:
			matches+=1
			if computer_choice==choices[0]:
				print("The computer won")
				computer+=1
			elif computer_choice==choices[1]:
				print("You won")
				player+=1
			else :
				print("Tied")
				tied+=1
		return  matches, player, computer, tied
		


	def help():
		print("\n")
		print("|--------------------HELP DESK---------------------|")
		print("Choose one of the choices...")
		print("Enter the serial number which is beside your choise.")
		print("AND thats it with this game....keep playing")
		print("|--------------------------------------------------|")


	def comp_choice(computer_choice):
		global computer,matches
		matches+=1
		print("The computer has chosen:" ,computer_choice,"\n")
		print("The computer won")
		computer+=1
		return computer,matches


	if normal:
		print("IF you wnt to quit type 'quit'.")


#----------------------------------NORMAL MODE------------------------------------#

	while True:

		if extreme or hard:
			break

		computer_choice=random.choice(choices)
		print("\n\n\n\nChoose any one of them\n0.HELP\n1.Rock \n2.Paper\n3.Scicors")
		user_choice=input("\nYour choice:").strip().upper()
		
		if user_choice=="QUIT":
			quit(matches,player,computer,tied)
			break
		
		try :
			user_choice=int(user_choice)
		except ValueError:
			print("\nerror :i can't understand you")
			continue
		
		if user_choice > 3:
			print("\n\nerror :its not an option")
			continue
		
		if user_choice== 0:
			help()
			continue
		
		print("\nPlayer choice:",shit[user_choice])
		print("The computer has chosen:" ,computer_choice,"\n")
		
		winner(user_choice,computer_choice)
		

#--------------------------------------------HARD MODE-------------------------------------#
	while True:
		if extreme or normal:
			break
		print("\n\n\n\nChoose any one of them\n0.HELP\n1.Rock \n2.Paper\n3.Scicors\ntype 'quit' to QUIT")
		user_choice=input("\nYour choice:").strip().upper()
		
		if user_choice=="QUIT":
			quit(matches,player,computer,tied)
			break
		
		try :
			user_choice=int(user_choice)
		except ValueError:
			print("\nerror :i can't understand you")
			continue
		
		if user_choice > 3:
			print("\n\nerror :its not an option")
			continue
		
		if user_choice== 0:
			help()
			continue

		print("\nPlayer choice:",shit[user_choice])
		

		if user_choice==1:
			computer_choice=random.choice(hard_rock)
			
		elif user_choice==2:
			computer_choice=random.choice(hard_paper)
			
		elif user_choice==3:
			computer_choice=random.choice(hard_scicors)
		print("The computer has chosen:" ,computer_choice,"\n")

		winner(user_choice,computer_choice)


#------------------------------------------------EXTREME MODE-----------------------------------------#
	while True:

		if hard or normal :
			break
		
		print("\n\n\n\nChoose any one of them\n0.HELP\n1.Rock \n2.Paper\n3.Scicors\ntype 'quit' to QUIT")
		user_choice=input("\nYour choice:").strip().upper()
		
		if user_choice=="QUIT":
			quit(matches,player,computer,tied)
			break
		
		try :
			user_choice=int(user_choice)
		except ValueError:
			print("error :i can't understand you")
			continue
		
		if user_choice > 3:
			print("\n\nerror :its not an option")
			continue
		
		if user_choice== 0:
			help()
			continue
		
		print("Player choice:",shit[user_choice])
		if user_choice==1:
			computer_choice=choices[1]
			comp_choice(computer_choice)

		elif user_choice==2:
			computer_choice=choices[2]
			comp_choice(computer_choice)
			
		elif user_choice==3:
			computer_choice=choices[0]
			comp_choice(computer_choice)





	still=input("Do you want to play again or do you want to quit?\nType your choise: ").strip().lower()	
	
	if still=='play again' or 'play' or 'again' or 'yes':
		print("\nLOOKING LIKE YOU LOVE TO PLAY THIS GAME.........")
		continue
	else:
		break





















