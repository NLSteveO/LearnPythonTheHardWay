# Imports argv from sys
from sys import argv

# Takes the two arguments from argv and sets them to variables
script, filename = argv

# Creates a variable and sets it to the file opened
txt = open(filename)

# Prints the filename
print "Here's your file %r:" % filename
# Prints the contents of the file
print txt.read()

# Asks the user for the filename again
print "Type the filename again:"
# Creates a variable and sets it to the filename given
file_again = raw_input("> ")

# Creates a variable and sets it to the file opened
txt_again = open(file_again)

# Prints the contents of the file
print txt_again.read()
