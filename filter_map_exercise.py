# Write a function called remove_negatives that accepts a list of numbers and
# returns a copy of the lists with all negative numbers removed. Use filter() in your implementation, not a list comprehension!

# remove_negatives([-1,3,4,-99])     #[3,4]

# remove_negatives([-7,0,1,2,3,4,5])      #[0, 1, 2, 3, 4, 5]

# remove_negatives([50,60,70])   #[50,60,70]


def remove_negatives(lista):
    return list(filter(lambda n: n >= 0, lista))


print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
