print "What is your first name?"
fname = raw_input('|--> ')
print "What is your last name?"
lname = raw_input('|--> ')
print "What is your middle initial?"
minitial = raw_input('|--> ')
print "What is your gender?"
gender = raw_input('|--> ')
name = fname + " " + minitial + ". " + lname

print "\nSo, your name is %r. \nYour gender is %r.\n\nNice to meet you!\n\n" % (name, gender)
