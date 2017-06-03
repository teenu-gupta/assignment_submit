import sys
sys.path.append("../")
from cleanwords import *
from word_freq import get_word_freq
from bigrams.word_freq_bigrams import get_line_bigrams, get_word_freq_bigrams
from word_freq_bigrams_noise_words_removed import load_noise_words
import random

def sort_words(word_list):
	sorted_list = sorted(word_list)
	return sorted_list

def create_tag_cloud(words_dict,sort_words,f,colors_list,cases_list):
	sort_freq = sorted(words_dict.values())
	sorted_list = []
	for i in sort_words:
		sorted_list.append((i,words_dict[i]))
	counter = 0 
	for i in sorted_list:
		counter +=1
		val = "<font size="+str(i[1])+" color=" + random.choice(colors_list) +" style=\"text-transform: "+random.choice(cases_list)+";>" + i[0] + "</font>"
		f.write(val)
		if counter%4 == 0:
			f.write("</br>")


if __name__ == '__main__':
	colors_list = ['blue','green','red','grey','black','yellow','orange']
	cases_list = ["uppercase","lowercase","capitalize"]
	line_list = []
	with open("../input_files/tags.txt","r") as f:
		line = f.readline()
		while line:
			cleaned_line = clean_words(line)
			line_list.append(cleaned_line)
			line = f.readline()
	noise_words = list(load_noise_words())
	
	cleaned_file = []
	for line_val in line_list:
		for i in line_val.split():
			if i not in noise_words:
				cleaned_file.append(i)

	file_data = ' '.join(cleaned_file)
	f1 = open("cleaned_data.txt","w")
	f1.write(file_data)
	f1.close()
	with open("cleaned_data.txt","r") as f1:
		bigram_freq_dict = get_word_freq_bigrams(f1)
		print bigram_freq_dict

	sort_words = sort_words(bigram_freq_dict.keys())
	print sort_words

	f = open("tagcloud_bigram.html","w")
	f.write("<html>")
	f.write("<body>")
	# f.write("<ul>")

	
	create_tag_cloud(bigram_freq_dict,sort_words,f,colors_list,cases_list)
	# f.write("</ul>")
	f.write("</body>")
	f.write("</html>")
	f.close()
		







