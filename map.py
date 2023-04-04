# The following code creates a list 'nums' containing 4 integers
nums = [2, 4, 6, 8]

# The map() function applies the lambda function to each element in 'nums', doubling each number
# The resulting list of doubled numbers is then converted to a new list using the list() function
doubles = list(map(lambda x: x*2, nums))

# The new list of doubled numbers is printed to the console
print(doubles)

# The following code creates a list 'people' containing 3 strings
people = ["adam", "badam", "tadam"]

# The map() function applies the lambda function to each element in 'people', converting each string to title case
# The resulting list of title-cased strings is then converted to a new list using the list() function
peeps = list(map(lambda name: name.title(), people))

# The new list of title-cased strings is printed to the console
print(peeps)

# The following code defines a function 'double' that takes in a number and doubles it


def double(x):
    return x*2


# The map() function applies the 'double' function to each element in 'nums', doubling each number
# The resulting iterable object is assigned to 'doubles2'
doubles2 = map(double, nums)

# The iterable object 'doubles2' is converted to a new list using the list() function and printed to the console
print(list(doubles2))
