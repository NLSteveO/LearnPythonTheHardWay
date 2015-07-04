from sys import argv

script, fname, lname = argv

name = fname + " " + lname

print "Hello %r," % (name)
print "You're running script: %r" % (script)

age = raw_input('How old are you? ')
eyecolor = raw_input('What color are your eyes? ')

print "So %r, you're %r years old and have %r eyes" % (
    fname, age, eyecolor)
