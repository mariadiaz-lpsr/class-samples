import random

guessnumber = random.randint(1, 5)
print("I'm thinking of a number between 1 and 5. Enter your guess!")
guess = input()

if guess < guessnumber:
	print("Nope, too low! Guess again.")
if guess > guessnumber:
	print("Nope, to high! Guess again.")
if guess == guessnumber:
	print("Hooray, you won!")

