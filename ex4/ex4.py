# Set variable cars
cars = 100
# Set variable space_in_a_car
space_in_a_car = 4.0
# Set variable drivers
drivers = 30
# Set varible passengers
passengers = 90
# Set variable cars_not_driven
cars_not_driven = cars - drivers
# Set variable cars_driven
cars_driven = drivers
# Set variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Set variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


# Print number of available cars
print "There are", cars, "cars available."
# Print number of drivers available
print "There are only", drivers, "drivers available."
# Print number of undriven cars
print "There will be", cars_not_driven, "empty cars today."
# Print carpool capacity."
print "We can transport", carpool_capacity, "people today."
# Print number of passengers
print "We have", passengers, "to carpool today."
# Print average passengers per car
print "We need to put about", average_passengers_per_car, "in each car."
