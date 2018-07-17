import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #turns the first letter uppercase(for words like Paris)
        return data[word.title()]
    elif word.upper() in data: #turns the word uppercase (for acronyms )like UN or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0: #searches for posible matches if the word is misspelled
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else: #for entries like assfhdskdf
        return "The word doesn't exist. Please double check it."

word = input("Enter a word here: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
