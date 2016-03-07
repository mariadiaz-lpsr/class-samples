class Player(object):
# we are defining the objects
        def __init__(self, name, age, goals, jersey, position):
                self.player_name = name
                self.player_age = age
                self.number_goals = goals
                self.jersey = jersey
                self.position = position
 
        # this adds each players name
        def printStats(self):
                print("Name: " + self.player_name)
                print("Age: " + str(self.player_age))
                print("Goals: " + str(self.number_goals))
                print("Jersey Number: " + str(self.jersey))
                print("Position: " + self.position)

# this will sae the team into the file
def saveTeam(playerList, filename):
	# it will open file and write on it 
        save_it = open((filename), 'a')
        for t in playerList:
                # make player_age and number_goals into strings and it will write in separate line 
		save_it.write(t.player_name + ' ' + str(t.player_age) + ' ' + str(t.number_goals) + str(t.jersey) + ' ' + t.position + '\n')
 	# the file will get closed now
        save_it.close()
 
 
def loadTeam(filename):
        team = []
        my_loadteam = open(filename, 'r')
        my_team = my_loadteam.readline()
        # the file is going to breakdown in small pieces
	while my_team != "":
		teamm = my_team.split()
                team.append(Player(teamm[0], teamm[1], teamm[2], teamm[3], teamm[4]))
                my_team = my_loadteam.readline()
 	# now the file will close
	my_loadteam.close()

	return team 

# it will ask the user these 2 statements below
print("choose one of these options below") 
print("(1) Start with a new team") 
print("(2) Open a file for an existing team") 
respond = raw_input()

# if the input was the number 5 it will ask the user for the file name they want to open for it can show their whole team
if respond == '2':
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	teamfile = raw_input()
	playerList = loadTeam(teamfile)
	print("You're good to go now,You are in your team file")

# if they entered number 4 it will make a new list
elif respond == '1':
	playerList = []
# if x is not equal to 0 it will just print out if you want to add, print, or save your players list
x = 1
while x != "0":
                print("(1)Add Players")
                print("(2) Print Players")
                print("(3) Save your player list to a file")
                print("(0) Leave program but before you should save it so you can avoid losing data")
                x = raw_input()
# whether the input was 1 it will ask for your name age goals jersey number and the position
		if x == "1":
                        print("Name:")
                        namersp = raw_input()
                        print("Age:")
                        agersp = raw_input()
                        print("Goals:")
                        goalsrsp = raw_input()
                        print("Jersey Number:")
                        jerseyrsp = raw_input()
                        print("Position:")
                        positionrsp = raw_input()

			# the list of the details will appened in the empty list
			playerList.append(Player(namersp, agersp, goalsrsp, jerseyrsp, positionrsp))


		# when the input is 2 it will print out all the status of all the players
		elif x == "2":
			for soccer in playerList:
                		soccer.printStats()
                # input is equal to 3 will save the list of players into the file ypu've created
		elif x == "3":
			print("You can save your team into a file using .tmd after the name")
			answerforfile = raw_input()
			saveTeam(playerList, answerforfile)
 
 
