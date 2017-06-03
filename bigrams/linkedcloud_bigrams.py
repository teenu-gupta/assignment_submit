import sys
sys.path.append("../")
from word_freq_bigrams_noise_words_removed import load_noise_words
from bigrams.word_freq_bigrams import get_line_bigrams, get_word_freq_bigrams
from cleanwords import *
from getwords import get_words
import random
import copy

def sort_words(word_list):
	sorted_list = sorted(list(set(word_list)))
	return sorted_list

def create_tag_cloud(words_dict,sort_words,f,colors_list,cases_list):
	
	
	sorted_list = []
	# for i in sort_words:
	# 	sorted_list.append(i,words_dict[i])
	sorted_words_unified = {}
	
	for i in sort_words:
		sorted_words_unified[i.replace(' ','_')]=i
		sorted_list.append(i.replace(' ','_'))
	counter = 0 
	for i in sorted_list:
		
		counter +=1
		val = "<font size="+str(words_dict[i]) +" id=\"" + str(i)+"\" onclick=\"reveal_sentences(this.id)\" color=" + random.choice(colors_list) +" style=\"text-transform: "+random.choice(cases_list)+"\";>" + i + "</font>"
		
		print val

		f.write(val)
		f.write("\n")
		if counter%4 == 0:
			f.write("</br>")
		
if __name__ == '__main__':
	colors_list = ['blue','green','red','grey','black','yellow','orange']
	cases_list = ["uppercase","lowercase","capitalize"]
	data = []
	line_dict = {}
	line_words_dict = {}
	line_count = 0

	with open("../input_files/tags.txt","r") as f:
		line = f.readline()
		while line:
			line_key_val = "sent_"+str(line_count)
			line_dict[line_key_val] = clean_words(line)
			line = f.readline()
			line_count +=1
	noise_words = list(load_noise_words())
	print line_dict 


	cleaned_line_dict = {}
	cleaned_line_val = []

	for sent_id,cleaned_line in line_dict.iteritems():
		val_cleaned = []
		for i in cleaned_line.split():
			if i not in noise_words:
				val_cleaned.append(i)
		
		input_val = ' '.join(val_cleaned)
		cleaned_line_dict[sent_id]=get_line_bigrams(input_val)
	
	
	cleaned_data_bigrams = {}
	bigrams = []
	for k,j1 in cleaned_line_dict.iteritems():
		bigram_list = []
		for val in j1:
			val1 = ' '.join(list(val))
			bigram_list.append(val1)
			bigrams.append(val1)
		cleaned_data_bigrams[k] = bigram_list
	
	
	print cleaned_data_bigrams
	
	words_freq_dict = {}
	sort_words = sort_words(bigrams)
	for i in sort_words:
		
		words_freq_dict[i.replace(' ','_')]=bigrams.count(i)
	print words_freq_dict
		
	f = open("main_page_bigrams.html","w")
	words_sent_dict = {}
	for word in sort_words:
		val = []
		for sent_id,bigrams_input in cleaned_data_bigrams.iteritems():
			if word in bigrams_input:
				val.append(sent_id)
		words_sent_dict[str(word.replace(" ","_"))] = (val)
	words_sent_dict = str(words_sent_dict).replace('\'',"\"")
	line_dict = str(line_dict).replace("\'","\"")

	f = open("main_page.html","w")
	f.write("<html>")
	f.write("\n")
	f.write("<head>")
	f.write("\n")
	f.write("<script type=\"text/javascript\">")
	f.write("\n")
	f.write("\n")
	f.write("function reveal_sentences(clicked_id){ ")
	f.write("\n")
	f.write("var obj1=")
	f.write(str(line_dict))
	f.write("\n")
	f.write("var obj2 =")
	f.write("\n")
	f.write(str(words_sent_dict))
	f.write("\n")
	f.write("var value = null;")
	f.write("\n")
	f.write("\t")
	f.write("var a= [];")
	f.write("\n")
	f.write("\t")
	f.write("var i=0;")
	f.write("\t")
	f.write("var j=0;")
	f.write("\n")
	f.write("for(var key in obj2)")	
	f.write("\t")
	f.write("\n")
	f.write("{")
	f.write("\n\t")
	f.write("if(String(key) == String(clicked_id)){a = obj2[key];}}")
	f.write("\n\t")
	f.write("document.getElementById(clicked_id).innerHTML = String(a);}")
	f.write("</script>")
	f.write("\n")
	f.write("<head>")
	f.write("\n")
	f.write("<body>")
	create_tag_cloud(words_freq_dict,sort_words,f,colors_list,cases_list)

	f.write("</body>")
	f.write("</html>")
	f.close()

	