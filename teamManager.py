class Player(object):
  def __init__(self, name, age, goals):
    self.name = name
    self.age = age
    self.goals = goals
    
print ''' (1) Make a Player
 (2) Make New Player
 (3) Print Average Stats
 (4) Exit Program'''
 
 
# The Creating Part
choice = int(input())
if choice == 1:
  print "What's your players name?"
  name = str(input())
  print "What's your players age"
  age = int(input())
  print 'How many goals has your player made?'
  goals = int(input())
 
print ''' 
 (2) Make New Player
 (3) Print Average Stats
 (4) Exit Program'''
choice = int(input())
if choice == 2:
  print "What's your players name?"
  name2 = str(input())
  print "What's your players age"
  age2 = int(input())
  print 'How many goals has your player made?'
  goals2 = int(input())
  
Player1 = Player((name), (age), (goals))
print Player1.name, Player1.age, Player1.goals 
Player2 = Player((name2), (age2), (goals2))
print Player2.name, Player2.age, Player2.goals 

print ''' 
 (3) Print Average Stats
 (4) Exit Program'''
choice = int(input())
if choice == 3:
  averageage = age * age2
  averageage = averageage * .5
  print('Average age = ' + str(averageage))
  averagegoals = goals * goals2
  averagegoals = averagegoals * .5
  print('Average age = ' + str(averageage))
