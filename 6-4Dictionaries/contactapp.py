myContacts = {}
count = 0
while count < 10:
	print("WELCOME TO THIS CONTACTS APP")	
	print("(1) Add a phone number")
	print("(2) Print the full list of contacts")
	print("(3) Enter a name to retrieve thats contact number")
	print("(0) Exit the CONTACTS APP")
	respond = int(input())
	if respond == 1:
		print("What's your name?")
		name = input()
		print("What's your phone number?")
		phone = input()
		myContacts[name] = phone
	elif respond == 2:
		print(myContacts)
	elif respond == 3:
		print("Whose number would you like")
		num = input()
		
	elif respond == 0:
		exit()
