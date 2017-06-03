# 1) Write a function getwords(text) to take a string, parse it and return words (tokens). 

import re

def get_words(text):
    output = re.split("\s|(?<!\d)[.,](?!\d)",text)
    return output

# print get_words("teenu   ")
    