import sys
sys.path.append("../")
from cleanwords import *
from bigrams.word_freq_bigrams import get_line_bigrams, get_word_freq_bigrams
from word_freq import get_word_freq

def load_noise_words():
    noise_words = set()
    with open("../input_files/noise_words.txt") as f:
        for line in f:
            try:
                word = line.strip().lower()
                noise_words.add(word)
            except:
                continue
    return noise_words



if __name__ == '__main__':
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


		


