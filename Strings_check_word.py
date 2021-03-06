# Takes a list of documents (each document is a string) and a keyword.
#  Returns True if a keyword is found, False when it's not.

    # Example:
    # doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    # >>> word_search(doc_list, 'casino')
    # >>> True


def word_search(doc_list, keyword):
    x = False
    for sentence in doc_list:
        sentence = sentence.split(sep=' ')
        for word in sentence:
            word = word.strip().lower()
            if word[-1] in ['.',',','!','?']:
                word = word[:-1]
            if word == keyword:
                x = True
            x = x or x
    print(x)

doc_list = ["They Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_search(doc_list,'they')


# Getting the index of the word in a sentence with the keyword in the list

def word_search(doc_list, keyword):
    result = []
    for sentence in doc_list:
        sentence = sentence.split(sep=' ')
        for i in range(0,len(sentence)):
            if sentence[i].lower().strip('.') == keyword:
                result.append(i)
    print(result)

word_search(doc_list, 'they')

# Getting the index of the sentence with the keyword in it
def word_search(doc_list, keyword):
    result = []
    for i,x in enumerate(doc_list):
        words = x.split()
        words = [a.rstrip('.,').lower() for a in words]
        if keyword.lower() in words:
            result.append(i)
    print(result)

word_search(doc_list, "car")




def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """

    result = {}
    for k in keywords:
         result[k] = word_search(doc_list, k)
    print(result)
keywords = ['test', 'the', 'car', 'casino']
multi_word_search(doc_list,keywords)