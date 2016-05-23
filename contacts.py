def ask():
	print('(1) Add Number')
	print('(2) Print List of Contacts & their numbers')
	print('(3) Find a Contact')
	print('(4) Exit')
def answer1():
	if answer == 1:
		print('okay')
		print('Whats your contacts name and number?(enter like name:number)')
		nameandnumber = str(input())
		contact.append(nameandnumber)
def answer2():
	if answer == 2:
		for names in contact:
			print(names)
def answer3():
	if answer == 3:
		print('What is your contacts name?')
		contactname = str(input())
def answer4():
	if answer == 4:
		print('Okay')
		print('bye')
	
contact = {}
contact = ['Garland']
ask()
answer = int(input())
if answer == 1:
	answer1()
if answer == 2:
	answer2()
if answer == 3:
	answer3()
ask()
answer = int(input())
if answer == 1:
	answer1()
if answer == 2:
	answer2()
if answer == 3:
	answer3()
	
# Farthest I got...
