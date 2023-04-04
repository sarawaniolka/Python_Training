# exercise to combine filter and map
# Given the list of names:
names = ['Lassie', 'Colt', 'Rusty', "Bob"]

# Return a new list wit the string:
# "Your instructor is" + each value in the array,
# but only if the value is less than 5 characters

short_names = list(filter(lambda name: len(name) < 5, names))
print(list(map(lambda name: f"Your instructor is {name}", short_names)))
