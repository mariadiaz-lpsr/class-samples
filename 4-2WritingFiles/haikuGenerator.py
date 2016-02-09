# it is just printing welcome the the generator and asking user for the first line of their haiku
print("Welcome to the Haiku Generator!")
# will ask for the lines of its haiku one by one 
print("Provide the first line of your haiku:")
# user writes the input to haiku
respond = raw_input()
print("Provide the second line of your haiku:")
answer = raw_input()
print("Provide the last line of you haiku:")
answerss = raw_input()
print("What file would you like to write your haiku to ?")
file_name = raw_input()
# whenever you try to put the cat 'file name' it will print the haiku you wrote
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")
# it will append the users input to the file
files = open((file_name), "a")
files.write(respond + '\n' + answer + '\n' + answerss + '\n')
# the files closes
files.close()
