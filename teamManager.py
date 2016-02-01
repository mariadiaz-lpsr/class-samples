class Player(object):
# we are defining the objects 
	def __init__(self, player_name, player_age, number_goals):
		self.player_name = player_name
		self.player_age = player_age
		self.number_goals = number_goals
			
	# this adds each players name  
	def printStats(self):
		print("Name: " + str(self.player_name))
		print("Age: " + str(self.player_age))
		print("Goals: " + str(self.number_goals))
# we are making an empty list named myPlayers
myPlayers = [] 
# it would print 4 different statements
print("Choose whether you want to add players or print players")
print("(1) Add Players")
print("(2) Print Players")
print("(3) To exit")
c = int(raw_input())
# it has a while loop when c is not equal to 3
while c != 3:
	 # if the input equals to 1 it will do the things below 
	if c == 1:
		print("Name:")
		choose = raw_input()
		print("Age:" )
		z = int(raw_input())
		print("Goals:")
		goals = int(raw_input())
		# the name age and goals been written will be put in the myPlayers list
		myPlayers.append(Player(choose, z, goals))
		print("Choose one option below")
		print("(1) Add Players")
		print("(2) Print Players")
		print("(3) To exit")
		c = int(raw_input())
	# the elif statement will only run if it equals to 2
	elif  c == 2 :
		print("The Stats of All the players")
		# we use a for statement 
		for soccer in myPlayers:
		# it will print the status of the players name,age,goals of all of the players you created 
			soccer.printStats()	
			c = int(raw_input())

