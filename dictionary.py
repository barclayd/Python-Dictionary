import json

# loads dictionary.json as a python dictionary
dictionary = json.load(open("dictionary.json"))
# check if word is in dictionary - handle words that aren't included in dictionary


def get_definition(word):

    if word in dictionary:

        return dictionary[word]
    else:
        return "The word doesn't exist, please double check it."


word_user = input("Enter a word: ")

print(get_definition(word_user))
