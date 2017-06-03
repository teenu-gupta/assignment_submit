
# put try catch block inside it
# handle numbers and spaces
#['hei', 'is', '1', 'yeasr', 'old', '', '']
# from utils.clean_words import remove_space,remove_apostrophes,remove_special_chars
import re
from getwords import get_words

__remove_spaces__ = re.compile("\s+")
__remove_special_chars = re.compile("[\(\)\[\]\{\}/\:;\*\'.\",<>?]+")
__remove_numbers = re.compile("\d+")

def remove_space(val):
    output = __remove_spaces__.sub(" ",val).strip()
    return output

def remove_numbers(val):
    output = __remove_numbers.sub(" ",val)
    return output

def remove_apostrophes(val):
    val = str(val).replace("'s"," ").strip()
    return val
    
def remove_special_chars(val):
    output = remove_apostrophes(val)
    output = __remove_special_chars.sub(" ",val).strip()
    return output

def remove_non_ascii_chars(val):
    output = ''.join(i for i in val if ord(i)<128)
    
def lowercase_conversion(val):
    output = val.lower()
    return output

def clean_words(text_val):
    val = remove_apostrophes(text_val)
    val = remove_special_chars(val)
    val = lowercase_conversion(val)
    val = remove_numbers(val)
    val = remove_space(val)
    return val
    
def get_line_tokens(line):
    tokenized_line = get_words(line)
    return tokenized_line

def output_words():
    input_string = raw_input("enter a string")
    val = clean_words(input_string)
    value =  get_line_tokens(val)
    print(value)

if __name__ =='__main__':
    output_words()
    
    
