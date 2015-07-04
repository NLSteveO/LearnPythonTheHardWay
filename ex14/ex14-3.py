from sys import argv

script, user_name, previous_score = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Do you think you can beat your previous score of %s?" % previous_score
answer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer. Nice.
And you said %r about beating your previous score.
""" % (likes, lives, computer, answer)
