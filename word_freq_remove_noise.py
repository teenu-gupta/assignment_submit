from cleanwords import *
from word_freq import get_word_freq

def load_noise_words():
    noise_words = set()
    with open("input_files/noise_words.txt") as f:
        for line in f:
            try:
                word = line.strip().lower()
                noise_words.add(word)
            except:
                continue
    return noise_words

# print load_noise_words()


def remove_noise_words(pre_word_list,noise_words_set,post_word_list=[]):
    post_word_list = pre_word_list - noise_words_set
    return post_word_list


if __name__ == '__main__':
    data = []
    with open("input_files/tags.txt","r") as f:
        words_freq_dict = {}
        # Before removing noise words
        words_freq = get_word_freq(f)
        print words_freq
        words_list = words_freq.keys()
        noise_words_set = load_noise_words()
        words_list_set = set(words_list)
        word_set_noise_words_removed = remove_noise_words(words_list_set,noise_words_set)
     
        #After removing noise words
        words_freq_list = {}
        for word in word_set_noise_words_removed:
            words_freq_dict.update({word:words_freq[word]})
        print len(words_freq_dict)

        print words_freq_dict





