import sys
sys.path.append("../")
from cleanwords import *


def get_line_bigrams(line_text):
	line_tokens = line_text.split()
	result = zip(line_tokens[:-1],line_tokens[1:])
	return result



def get_word_freq_bigrams(f):
	line = f.readline()
	words_freq = {}
	file_bigram_list = []
	while line:
		print line
		val = clean_words(line)
		file_bigram_list.extend(get_line_bigrams(val))
		line = f.readline()
	# print(file_bigram_list)
	file_bigram_list_set = set(file_bigram_list)
	
	bigrams = [i[0] +" "+ i[1] for i in file_bigram_list_set]
	
	for i in bigrams:
		words_freq.update({i:bigrams.count(i)})
	return words_freq


if __name__ == '__main__':
	with open("../input_files/tags.txt","r") as f:
		get_word_freq_bigrams_dict = get_word_freq_bigrams(f)
		print get_word_freq_bigrams_dict
		print len(get_word_freq_bigrams_dict)


