# The following code creates a list 'l' containing 4 integers
l = [1, 2, 3, 4]

# The filter() function is used to filter out all the odd numbers in 'l'
# The lambda function checks if a number is even or not by checking if its remainder is 0 when divided by 2
# The resulting list of even numbers is then converted to a new list using the list() function
evens = list(filter(lambda x: x % 2 == 0, l))

# The new list of even numbers is printed to the console
print(evens)

# The following code creates a list 'names' containing 5 strings
names = ["Adam", "Adriana", "Bob", "Alice", "Celine"]

# The filter() function is used to filter out all the names in 'names' that start with the letter 'A'
# The lambda function checks if the first character of each string is 'A'
# The resulting list of names that start with 'A' is then converted to a new list using the list() function
a_names = list(filter(lambda name: name[0] == "A", names))

# The new list of names that start with 'A' is printed to the console
print(a_names)
