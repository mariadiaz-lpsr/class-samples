import string 
# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
#
# Author: rc.diaz.maria [at] leadps.org

# makes a maping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters  
def  createDictionary(key):
	
	# placeholder
	alphabet = string.ascii_lowercase
	alphabett = string.ascii_uppercase
	# created a dictionary named alphabet1
	alphabet1 = {}
	
	for h in range(0, len(alphabet)):
		alphabet1[alphabet[(h - key) % 26]] = alphabet[h]
		
	# the range of 0 to the length of alphabet it will be subtracted by the number of key then divided by 26 which is the number of the length if list
	for h in range(0, len(alphabett)):
		alphabet1[alphabett[(h - key) % 26]] = alphabett[h]

	# chr returns a string for lowercase and uppercase in a range of 32, 64
	for h in range(32, 64):
		alphabet1[chr(h)] = chr(h)
		
		return alphabet1
# get the encoded message	
# arguments: none
# returns: encoded message
def getMessage():
		print("Now what message do you want to encode with the key:")
		# user inputs the word they want to be encoded for it can return it
		encoded = input()
		return encoded
	
# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	decode = ''
	for jidoublemy in message:
		decode = decode + dictionary[jidoublemy]
	return decode
	

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
# it will print the decoded message
def printMessage(message):
	print(message)


# execution starts here

# ask user for key
print("What key would you like to use to decode?")
key = int(input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)

printMessage(decodedMessage)
