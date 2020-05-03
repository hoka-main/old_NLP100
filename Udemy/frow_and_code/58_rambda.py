l = ['Mon', 'tue', 'Wed', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sumple_func(word):
    return word.capitalize()

def sumple_func2(word):
    return word.lower()



# sample_func = lambda  wprd:word.capitalize()

change_words(l, lambda word: word.capitalize())

change_words(l, lambda word: word.lower())

