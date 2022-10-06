# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. Save it to a variable called answer.

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]


answer = {list1[i]:list2[i] for i in range (0,3)}
print(answer)

# Given a person variable:

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]] 

# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value.  That's a terrible explanation.  I think it'll be easier if you just look at the end goal:
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'} 
answer = {person[i][0]:person[i][1] for i in range(0,3)}
print(answer)

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
answer = {i:0 for i in 'aeiou'}
print(answer)

#ASCII dictionary
answer = {'chr('+str(i)+')': chr(i) for i in range(65,91)}
print(answer)