print("Welcome to Maria's Quest!!") 
print("Enter the name of your character:")
character = raw_input()

print("Enter Strength (1-10):")
strength = int(input())

print("Enter Health (1-10):")
health = int(input())
 
print("Enter Luck (1-10):")
luck = int(input())
if strength + health + luck > 15:
	print("You have give your character too many points! ")
while strength + health + luck < 15: 
	print(character , "strength" + strength + "health" + health + "luck" + luck)
if strength + health + luck == 15:
	print(character," you've come to a fork in the road. Do you want to go right or left? Enter right or left. ")
if right or left == "left":
	print("Sorry you lost the game.")
# if user chooses right and has strength over 7
if strength >= 7:
	print(character,"you're strength is high enough you survived to fight the ninjas that attacked you. You won the game!")
else:
	print("You didn't have sufficient strength to defeat the ninjas. Sorry you lost the game :(. ")
# if health is greater than 8 
if health >= 8:
	print("You had enough energy to pass by the ninjas."
else:
	print("Sorry your health was not enough to survive the spriral ninja stars wound. ")
# if the number of luck is greater than 5 it wil print out the first line if not it will directly go to the else line
if luck >= 5:
	print("You had ")
