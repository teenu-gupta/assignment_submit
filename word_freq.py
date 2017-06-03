from cleanwords import *

def get_word_freq(f):
	line = f.readline()
	words_freq = {}
	file_words_list = []

	while line:
		print line
		val = clean_words(line)
		file_words_list.extend(get_line_tokens(val))
		line = f.readline()

	print(file_words_list)

	file_words_list_set = set(file_words_list)
	for i in file_words_list_set:
		words_freq.update({i:file_words_list.count(i)})
	return words_freq


if __name__ == '__main__':
	with open("input_files/tags.txt","r") as f:
		print get_word_freq(f)
		print len(get_word_freq(f))







