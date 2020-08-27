import json
import os
from difflib import get_close_matches
import mysql.connector

#load a json of the english dictionary
data = json.load(open("data.json"))


def dict_func(w):
    w = w.lower()
 
    #check if the key already exists and if it does, return the definition
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    
    #if an exact key doesnt exist, check for a close match
    elif len(get_close_matches(w, data.keys())) > 0:

        #Ask the user if that's the value they meant instead
        concur_var = input("Did you mean >> %s <<  instead? Enter Y for Yes or N for No:   " %get_close_matches(w, data.keys())[0])
        if concur_var == 'Y':
            return data[get_close_matches(w, data.keys())[0]]

        elif concur_var == 'N':
            return 'Your word doesnt exist. Please check the spelling.'
        else:
            return 'Input not recognized'


    #or give up, the word isn't a real word or they really buggered it up
    else:
        return 'Your word doesnt exist. Please check the spelling.'
    
#prompt the user

word = input("Enter word to lookup: ")

output = dict_func(word)

# check if it's a list vs a string before output
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)
