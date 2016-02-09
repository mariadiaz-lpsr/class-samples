# this would just print the string
print("Hey, Welcome to the Haiku Reader!")
 
print("Pick one of these Haiku") 
# user has to choose 3 or 4
print("(3) For a haiku about a mirror related") 
print("(4) For a haiku about the haikus been easy..") 
# it will just open both haikus-3 and 4
MyHaiku3 = open('haiku3.txt', 'r')
MyHaiku4 = open('haiku4.txt', 'r')
# the users answer is turning into an int
option = int(raw_input()) 
# if the user chose 3 it will print out that haiku
if option == 3:
	print(MyHaiku3.read())
# option equals to 4 and not 3 it will just print out 4th haiku	
elif option == 4:
	print(MyHaiku4.read())

