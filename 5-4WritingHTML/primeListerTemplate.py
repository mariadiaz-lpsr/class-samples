# returns True if myNum is prime 
# returns False is myNum is composite
def isPrime(x, myNum):
	# here is where it will have a certain range from 1 to 10000 
	y = range(2,int(x))
	# subtract each first to 2
	primenum = x - 2
	count = 0 
	for prime in y:
		# the number that was divided will then be divided to find remainder
		rem_prime = int(x) % int(prime)
		if rem_prime != 0:
			count = count + 1
		# if it is prime it will print it and append it to the listofprime
		if count == primenum:
			print(x)
			myNum.append(x)
ListOfPrime = []
# the file numbers.txt will open so it can be append the numbers that are prime only
prime = open("numbers.txt", "w")
# the range is from 2 to 100000
r = range(2, 100000)
for PList in r:
	numberss =  isPrime(PList, ListOfPrime)
for y in ListOfPrime:
	# the prime numbers will be written in a single list
	prime.write(str(y) + "\n")
# the file that was open "numbers.txt" will close
prime.close()		
		
