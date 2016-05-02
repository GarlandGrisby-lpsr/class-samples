 # '__init__' makes the player have a name, age, goals, and jersey number.
class Player(object):
        def __init__(self, name, age, goals, jersey_number, position):
                self.name = name
                self.age = age
                self.goals = goals
                self.jersey_number = jersey_number
                self.position = position
        def printStats(self):
                print("\n")
                print("Name: " + self.name)
                print("Age: " + str(self.age))
                print("Goals: " + str(self.goals))
                print("Jersey Number: " + str(self.jersey_number))
                print("Position: " + str(self.position))
                print("\n")
# allows the plaeyr to save the team
def saveTeam(playerList, filename):
        # opens the team file
        my_file = open(filename + '.tmd', 'w')
        for p in playerList:
                my_file.write(p.name + ' '
                                + str(p.age) + ' '
                                + str(p.goals) + ' '
                                + str(p.jersey_number) + ' '
                                + p.position + '\n')
        # closes the team file
        my_file.close()
# Makes a function for loading a team
def loadTeam(filename):
        my_players = []
        # opens the file
        my_file = open(filename, 'r')
        # reads each line
        line = my_file.readline()
        while line:
                # split each line into a list of the variables
                player = line.split()
                my_players.append(Player(player[0],
                        player[1],                                                                        
                        player[2],
                        player[3],
                        player[4]))
                 # read the next line
                line = my_file.readline()
        # closes the file
        my_file.close()
        # return the completed list
        return my_players
# Lets the user have a choice in what he wants to do
print("Welcome to Team Manager Deluxe!")
 
print("Do you want to start with a new team or open an existing team?")
 
print("Enter the number of your choice to choose.")
 
print("(1) Make a new team")
 
print("(2) Open a team file")

user_choice = int(raw_input())
 
if user_choice == 2:
        print("What's the filename?")
        filename = raw_input()
        my_players = loadTeam(filename)
 
else:   
        my_players = []
 
while user_choice != 0:
        print("What do you want to do? Enter the number of your choice and press Enter.")
        print("(1) Add a player?")
        print("(2) Print all players?")
        print("(3) Print average number of goals for all players?")
        print("(4) Save player to a file?")
        print("(0) Leave the program?")
        user_choice = int(raw_input())
        # if user adds player, get name, age, goals, and jersey number
        if user_choice == 1:
                print("Enter name:")
                player_name = raw_input()
                print("Enter age:")
                player_age = int(raw_input())
                print("Enter number of goals scored this season:")
                player_goals = int(raw_input())
                print("Enter the jersey number worn by this player:")
                jersey_num = int(raw_input())
                print("Enter the position that this player plays:")
                position = raw_input()
                my_players.append(Player(player_name, player_age, player_goals, jersey_num, position))
                print("Ok, player entered.")
        # If user chooses '2', it prints the players.
        if user_choice == 2:
                print("Here are all the players...")
                for player in my_players:
                        player.printStats()
 
        if user_choice == 3:
        # prints average stats
                sum = 0
                count = 0
                for player in my_players:
                        sum += player.goals
                        count += 1
                avg = sum / count
                print("Average goals: " + str(avg))
 
        if user_choice == 4:
                print("Ok, what would you like to name the file? We'll add on a .tmd file extension to wh$
                filename = raw_input()
                saveTeam(my_players, filename)
