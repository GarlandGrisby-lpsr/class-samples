# Making functions & classing
class Player(object):
	def __init__(self, name, age, goals, position):
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

# Starts the code execution
firstquestion()
User_Choice = int(raw_input())
if User_Choice == 1:
	openingfiles()
		
if User_Choice == 2:
	askquestions()
	userchoice = int(raw_input())	
	if userchoice == 1:
		print 'Whats your players name?'
		name = str(raw_input())
		print 'Whats your players age?'
		age = int(input())
		print 'Whats your players goals?'
		goals = int(raw_input())
		print 'Whats your players position?'
		position = str(raw_input())

print 'One more player'		
askquestions()







# Exit
if userchoice == 3:
	print 'Bye'
