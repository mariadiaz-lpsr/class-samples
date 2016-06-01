# CS 6.5 Tools for Ciphers - Indpendent Practice
# Implement the functions below - when you've finished, all tests should pass
# Author: [Maria Diaz]


# import statements here
import string


# calls function to create a list with the letters from a to z
# DOES NOT manually create the list
# use Google and/or Stack Overflow to find how to do this in python!
# returns a list with the lowercase letters a to z
def getLowercaseAlphabet():
	return ['a', 'b' ,'c', 'd', 'e', 'f', 'g','h',	'i',	'j', 'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r' ,'s' ,'t', 'u' ,'v' ,'w','x','y' ,'z']
	
def getUppercaseAlphabet():
	return['A', 'B' ,'C', 'D', 'E', 'F', 'G','H',	'I',	'J', 'K',	'L',	'M',	'N',	'O',	'P',	'Q','R' ,'S' ,'T', 'U' ,'V' ,'W','X','Y' ,'Z']
		
def getReorderedLowercaseAlphabet(key):
	return['f', 'g','h',	'i',	'j', 'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r' ,'s' ,'t', 'u' ,'v' ,'w','x','y' ,'z','a', 'b' ,'c', 'd', 'e']



# DO NOT EDIT THE TESTS BELOW HERE!
# ------------
#

low_alpha = getLowercaseAlphabet()

try:

    if(low_alpha[5] == 'f' and low_alpha[9] == 'j'):
        print("Test 1 passes! getLowercaseAlphabet() is correct.")
    else:
        print("Test 1 fails. getLowercaseAlphabet() needs more work.")
except:
    print("Test 1 fails. getLowercaseAlphabet() needs more work.")



high_alpha = getUppercaseAlphabet()

try:
    if(high_alpha[7] == 'H' and high_alpha[11] == 'L'):
        print("Test 2 passes! getUppercaseAlphabet() is correct.")
    else:
        print("Test 2 fails. getUppercaseAlphabet() needs more work.")
except:
    print("Test 2 fails. getUppercaseAlphabet() needs more work.")




reorderAlphabet = getReorderedLowercaseAlphabet(5)

try:
    if(reorderAlphabet[5]) == 'k':
        print("Test 3 passes! getReorderedLowercaseAlphabet() is correct.")
    else:
        print("Test 3 fails. getReorderedLowercaseAlphabet() needs more work.")
except: 
    print("Test 3 fails. getReorderedLowercaseAlphabet() needs more work.")
