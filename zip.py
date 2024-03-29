nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]
z = zip(nums1, nums2)
print(list(z))  # it's pairing into tuples

nums3 = [1, 2]
z2 = zip(nums3, nums1)
print(list(z2))  # stops when we go through all of the elements of the shorter list

# unziping
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
uz = list(zip(*five_by_two))
print(uz)


# Example: students' results
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['Kate', 'Ann', 'Sophia']

# dictionary comprehension
best_results = [max(pair) for pair in zip(midterms, finals)]
print(best_results)

final_grades = {pair[0]: max(pair[1:2])
                for pair in zip(students, midterms, finals)}
print(final_grades)

# map
scores = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

print(dict(scores))

# Exercise: write a function that accepts two strings and returns a string containing the 2 strings intersoven or zipped together.
# example: interleave('hi', 'ha) #hhia


def interleave(string1, string2):
    return ''.join(''.join(x) for x in zip(string1, string2))


print(interleave('test', 'back'))

# Exercise: write a function that accepts a list of numbers, filters out every number not divisible by 4 and returns a new list where every remaining number is tripled


def triple_and_filter()
