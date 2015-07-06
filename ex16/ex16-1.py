# Importing argv from sys library
from sys import argv

# Creating variables to hold the arguments from argv
script, filename = argv

# Print out the filename given as second argument
print "We're going to erase %r." % filename
# Print the option to stop now and how to do it
print "If you don't want that, hit CTRL-C (^C)."
# Print the option to continue and how to do it.
print "IF you do want that, hit RETURN."

# Taking user input to give chance to quit. Does nothing with the input if continued
raw_input("?")

# Print that we are opening the file so the user knows what is happening
print "Opening the file..."
# Open file with given filename and mode 'w' and save to variable
target = open(filename, 'w')

# Print that we are truncating the file so the user knows what is happening
print "Truncating the file. Goodbye!"
# Truncate the file
target.truncate()

# Print that you want the user to give you 3 lines of text
print "Now I'm going to ask you for three lines."

# Get line 1 and set to a variable
line1 = raw_input("line 1: ")
# Get line 2 and set to a variable
line2 = raw_input("line 2: ")
# Get line 3 and set to a variable
line3 = raw_input("line 3: ")

# Print that you will now write those lines to a file
print "I'm going to write these to the file."

# Write line 1 to file
target.write(line1)
# Write a newline to the file
target.write("\n")
# Write line 2 to file
target.write(line2)
# Write a newline to the file
target.write("\n")
# Write line 3 to file
target.write(line3)
# Write a newline to the file
target.write("\n")

# Print that you are now going to close the file
print "And finally, we close it."
# Close the file
target.close()
