# Takes a list of documents (each document is a string) and a keyword.
#  Returns True if a keyword is found, False when it's not.

    # Example:
    # doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    # >>> word_search(doc_list, 'casino')
    # >>> True


def word_search(doc_list, keyword):
    x = False
    for sentense in doc_list:
        sentense = sentense.split(sep=' ')
        for word in sentense:
            word = word.strip().lower()
            if word[-1] in ['.',',','!','?']:
                word = word[:-1]
            if word == keyword:
                x = True
            x = x or x
    print(x)

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_search(doc_list,'casino')