import json

from difflib import get_close_matches

# loads dictionary.json as a python dictionary
dictionary = json.load(open("dictionary.json"))
# check if word is in dictionary - handle words that aren't included in dictionary


def get_definition(word):

    # check for case sensitivity
    word = word.lower()

    if word in dictionary:

        return dictionary[word]

    elif word.title() in dictionary:

        return dictionary[word.title()]

    elif word.upper() in dictionary:

        return dictionary[word.upper()]
    # if word isn't found, check if there are closely matched alternatives
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        action = input("Hmm that doesn't seem right, did you mean %s instead? [y/n]: "
                       % get_close_matches(word, dictionary.keys())[0])
        if action == "y":
            return dictionary[get_close_matches(word, dictionary.keys())[0]]
        elif action == "n":
            return "That word doesn't exist"
        else:
            return "Can't make sense of your input, please try again"


user_word = input("Enter a word: ")

output = get_definition(user_word)

# if a word has multiple definitions, print them all
if type(output) == list:
    for item in output:
        print("--", item)
else:
    print("--", output)
