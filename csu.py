print("How many miles do you live from Richmond State?")
miles = int(raw_input())

print("What is your GPA?")
gpa = float(input())

print("What is your ACT score?")
act = int(raw_input())

if miles < 30:
	print("You live in local region")
	if gpa >= 2.0 and act >= 18:
		print("You've been accepted")
	else:
		print("You haven't been accepted")
else:
	print("You're not in the local region")
	if gpa >= 2.5 and act >= 18:
		print("You've been  accepted")
	else:
		print("You haven't been accepted")
  
