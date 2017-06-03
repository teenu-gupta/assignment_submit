from word_freq_remove_noise import *
from cleanwords import *
from word_freq import get_word_freq
from getwords import get_words
import random
import copy

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
		val = "<font size="+str(i[1]) +" id=\"" + str(i[0])+"\" onclick=\"reveal_sentences(this.id)\" color=" + random.choice(colors_list) +" style=\"text-transform: "+random.choice(cases_list)+"\";>" + i[0] + "</font>"
		f.write(val)
		f.write("\n")
		if counter%6 == 0:
			f.write("</br>")
		


if __name__ == '__main__':
	colors_list = ['blue','green','red','grey','black','yellow','orange']
	cases_list = ["uppercase","lowercase","capitalize"]
	data = []
	line_dict = {}
	line_words_dict = {}
	line_count = 0
	#make a line dict along with line ids

	f = open("input_files/tags.txt","r")
	lines = f.readlines()
	for line in lines:
		line_key_val = "sent_"+str(line_count)
		line_dict[line_key_val] = clean_words(line)
		line = f.readline()
		line_count +=1
	# print line_dict
	line_dict_copy = copy.deepcopy(line_dict)
	for i,k in line_dict_copy.iteritems():
		if len(k) == 0:
			del line_dict[i]


	for line_id,sentence in line_dict.iteritems():
		word_tokens= get_words(clean_words(sentence))
		line_key = line_id
		line_dict.update({line_key:(sentence)})
		# line_words_dict.update({line_id:(sentence,tuple(word_tokens))})
		line_words_dict.update({line_key:str(word_tokens)})

	# print line_dict
	# print line_words_dict
	f.close()
		# Before removing noise words
	f = open("input_files/tags.txt","r")
	words_freq = get_word_freq(f)
	words_list = words_freq.keys()
	noise_words_set = load_noise_words()
	words_list_set = set(words_list)
	word_set_noise_words_removed = remove_noise_words(words_list_set,noise_words_set)

	#After removing noise words
	words_freq_list = {}
	for word in word_set_noise_words_removed:
		words_freq_list.update({str(word):str(words_freq[word])})

	sort_words = sort_words(words_freq_list.keys())
	print sort_words
	f.close()
	words_sent_dict = {}

	for word in sort_words:
		val = []
		for sent_id,sent_tokens in line_words_dict.iteritems():
			if word in sent_tokens:
				val.append(sent_id)
		words_sent_dict[str(word)]=(val)
	

	words_sent_dict_copy = copy.deepcopy(words_sent_dict) 
	for i,k in words_sent_dict_copy.iteritems():
		if len(i) == 0:
			del words_sent_dict[i]
	
	# for key,value in words_sent_dict.iteritems():
	# 	sentence_val = []
	# 	for sent_id in value:
	# 		sentence_val.append(line_dict[sent_id])
	# 	words_sent_dict[key]=str(sentence_val)

	print str(words_sent_dict).replace("\'","\"")
	line_dict = str(line_dict).replace("\'","\"")
	words_sent_dict = str(words_sent_dict).replace('\'',"\"")
	line_words_dict = str(line_words_dict).replace('\'',"\"")

	print str(line_dict).replace("\'","\"")
	print str(words_sent_dict).replace('\'',"\"")
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
	f.write(line_dict)
	f.write("\n")
	f.write("var obj2 =")
	f.write("\n")
	f.write(words_sent_dict)
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
	create_tag_cloud(words_freq_list,sort_words,f,colors_list,cases_list)
	f.write("</body>")
	f.write("</html>")
	f.close()

	