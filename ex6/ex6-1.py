# Setting formatted string variable to print later
x = "There are %d types of people." % 10
# Set two simple strings to be formatted into a formatted string
binary = "binary"
do_not = "don't"
# Set formatted string to be printed later
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the two formatted strings previously created
print x
print y

# Print two formatted strings with the previous formatted strings
print "I said: %r." % x
print "I also said: '%s'." % y

# Set variable of boolean value False
hilarious = False
# Set string variable with format at the end to take another variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Print string variable inserting boolean variable
print joke_evaluation % hilarious

# Set two simple string variables
w = "This is the left side of..."
e = "a string with a right side."

# Print the two strings concatenated
print w + e
