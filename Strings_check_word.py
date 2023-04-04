# Takes a list of documents (each document is a string) and a keyword.
#  Returns True if a keyword is found, False when it's not.

# Example:
# doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
# >>> word_search(doc_list, 'casino')
# >>> True


# The following code defines a function 'word_search' that takes in a list of documents (strings) and a keyword.
# The function searches for the keyword in each document, and returns True if the keyword is found in any document, False otherwise.
def word_search(doc_list, keyword):
    x = False
    for sentence in doc_list:
        sentence = sentence.split(sep=' ')
        for word in sentence:
            word = word.strip().lower()
            if word[-1] in ['.', ',', '!', '?']:
                word = word[:-1]
            if word == keyword:
                x = True
            x = x or x
    print(x)


# An example list of documents and a keyword are defined, and the 'word_search' function is called with these arguments.
doc_list = ["They Learn Python Challenge Casino.",
            "They bought a car", "Casinoville"]
word_search(doc_list, 'they')

# The following code defines a function 'word_search' that takes in a list of documents (strings) and a keyword.
# The function searches for the keyword in each document, and returns a list of indices for the words in each sentence of each document that match the keyword.


def word_search(doc_list, keyword):
    result = []
    for sentence in doc_list:
        sentence = sentence.split(sep=' ')
        for i in range(0, len(sentence)):
            if sentence[i].lower().strip('.') == keyword:
                result.append(i)
    print(result)


# An example list of documents and a keyword are defined, and the 'word_search' function is called with these arguments.
doc_list = ["They Learn Python Challenge Casino.",
            "They bought a car", "Casinoville"]
word_search(doc_list, 'they')

# The following code defines a function 'word_search' that takes in a list of documents (strings) and a keyword.
# The function searches for the keyword in each document, and returns a list of indices for the documents that contain the keyword.


def word_search(doc_list, keyword):
    result = []
    for i, x in enumerate(doc_list):
        words = x.split()
        words = [a.rstrip('.,').lower() for a in words]
        if keyword.lower() in words:
            result.append(i)
    print(result)


# An example list of documents and a keyword are defined, and the 'word_search' function is called with these arguments.
doc_list = ["They Learn Python Challenge Casino.",
            "They bought a car", "Casinoville"]
word_search(doc_list, "car")

# The following code defines a function 'multi_word_search' that takes in a list of documents (strings) and a list of keywords.
# The function searches for each keyword in each document, and returns a dictionary where each key is a keyword, and the value is a list of indices for the documents that contain the keyword.


def multi_word_search(doc_list, keywords):
    result = {}
    for k in keywords:
        result[k] = word_search(doc_list, k)
    print(result)


# An example list of documents and a list of keywords are defined, and the 'multi_word_search' function is called with these arguments.
doc_list = ["The Learn Python Challenge Casino.",
            "They bought a car and a casino", "Casinoville"]
keywords = ['test', 'the', 'car', 'casino']
multi_word_search(doc_list, keywords)
