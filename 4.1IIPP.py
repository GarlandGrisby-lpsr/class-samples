# Asks the player what
print ''' Hi, welcome to the Haiku Reader! 
 Choose... 
 (3) For a haiku about a silly person.
 (4) For a haiku about writing haikus.'''
choice = int(input())
if choice == 3:
	Thirdhaiku = open('haiku3.txt', 'r')
	print(Thirdhaiku.read()) 
if choice == 4:
        fourthhaiku = open('haiku4.txt', 'r')
        print(fourthhaiku.read())

