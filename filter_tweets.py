# Create a dictionary of user data, where each key is a unique user ID and each value is a dictionary
# with the user's username and a list of their tweets
users = {"user1": {"username": "johndoe", "tweets": ["Hello, world!"]},
         "user2": {"username": "janedoe", "tweets": []},
         "user3": {"username": "jimmy", "tweets": ["This is my first tweet!", "I love coding!"]},
         "user4": {"username": "jenny", "tweets": []}
         }

# Filter the list of users to find those without any tweets, using a lambda function as the filter criterion
# The filter() function returns a new list containing only the elements from the original list that meet the filter criterion
inactive = list(filter(lambda user: len(user['tweets']) == 0, users.values()))

# Print the list of inactive users (i.e. those without any tweets)
print(inactive)

# Second approach (shorter), based on the fact that lists are falsy
inactive = list(filter(lambda user: not user['tweets'], users.values()))
print(inactive)


# Only collect usernames of inactive ones
inactive_names = list(map(lambda user: user['username'], filter(
    lambda user: not user['tweets'], users.values())))
print(inactive_names)
