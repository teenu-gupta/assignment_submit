from word_freq_remove_noise import *
from cleanwords import *
from word_freq import get_word_freq
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
		if counter%6 == 0:
			f.write("</br>")
		


if __name__ == '__main__':


	colors_list = ['blue','green','red','grey','black','yellow','orange']
	cases_list = ["uppercase","lowercase","capitalize"]
	data = []
	with open("input_files/tags.txt","r") as f:
		# Before removing noise words
		words_freq = get_word_freq(f)
		words_list = words_freq.keys()
		noise_words_set = load_noise_words()
		words_list_set = set(words_list)
		word_set_noise_words_removed = remove_noise_words(words_list_set,noise_words_set)

		#After removing noise words
		words_freq_list = {}
		for word in word_set_noise_words_removed:
			words_freq_list.update({word:words_freq[word]})
			print len(words_freq_list)

			print words_freq_list

		sort_words = sort_words(words_freq_list.keys())
		print sort_words

		f = open("tagcloud.html","w")
		f.write("<html>")
		f.write("<body>")
		
		
		create_tag_cloud(words_freq_list,sort_words,f,colors_list,cases_list)
		
		f.write("</body>")
		f.write("</html>")
		f.close()
		







