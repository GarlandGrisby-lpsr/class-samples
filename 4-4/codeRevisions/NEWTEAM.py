# Making functions & classing
class Player(object):
	def __init__(self, name1, age1, goals1, position1):
		self.name = name
		self.age = age
		self.goals = goals
		self.position = position
class Playertwo(object):
	def __init__(self, name2, age2, goals2, position2):
		self.name2 = name2
		self.age2 = age2
		self.goals2 =- goals2
		self.position2 = position2


def firstquestion():
	print'''Would you like to 
	(1)Open an older file?
	or
	(2) Make a new file?'''
def askquestions():
	print '''Would you like to 
	 (1) Make a new player?
	 (2) Print Average stats?
	 (3) Exit?
	'''

def openingfiles():
	print 'What is your files name?'
	file_name = str(raw_input())
	file = open('pumas.tmd', 'r')
	print(file.read())

def TwoPaverage():
	print 'The average age is ' + (age1 * age2 % 2)
	print 'The average goals are ' + (goals1 * goals2 % 2)




# Starts the code execution
firstquestion()
User_Choice = int(raw_input())
if User_Choice == 1:
	openingfiles()
		
if User_Choice == 2:
	askquestions()
	userchoice = int(raw_input())
	Numofplayers = 0	
	if userchoice == 1:
		print 'Whats your players name?'
		name1 = str(raw_input())
		print 'Whats your players age?'
		age1 = int(input())
		print 'Whats your players goals?'
		goals1 = int(raw_input())
		print 'Whats your players position?'
		position1 = str(raw_input())
		Numofplayers = Numofplayers + 1


		print 'One more player'		
		askquestions()
		userchoice = int(raw_input())
		if userchoice == 1:
			print 'Whats your players name?'
			name2 = str(raw_input())
			print 'age'
			age2 = int(raw_input())
			print 'Goals?'
			goals2 = int(raw_input())
			print 'Position?'
			position2 = str(raw_input())
			Numofplayers = Numofplayers + 1

			print '''Would you like to
			(2) Print average stats of players
			or
			(3) Exit?'''
			
			userchoice = int(raw_input())
			if userchoice == 2:
				TwoPaverage()

# Exit\
if userchoice == 3:
	print 'Bye'
