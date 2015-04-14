name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
metric_height = height * 2.54 #centimeters
weight = 180 #lbs
metric_weight = weight * 0.453592 #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That is %d centimeters." % metric_height
print "He's %d pounds heavy." % weight
print "That is %d kilograms." % metric_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)
