In the assignment folder - run command python filename.py


1) Write a function getwords(text) to take a string, parse it and return words (tokens).


  -- getwords.py


2) clearnwords.py -  Modify getwords and call it cleanwords(text). Cleanwords removes punctuation,
removes words which are just numbers, convert all words to lower case and return them.

--clean_words.py
 
3) word_freq.py - open a text file, read the text, process it using clearnwords.
Count the number of occurences of each unique word.

-- word_freq.py
 
4) Modify wordfreq.py to open a second file that contains only noise words.
Create a word frequency eliminating all the noise words. 

--- word_freq_remove_noise.py
 
5) tagcloud.py - Use wordfreq to generate a html tag cloud (an html tag cloud displays words in alphabetical order.
The higher the word frequency, the bigger the word.
 
 --- tag_cloud.py

6) linkedcloud.py - Modify tagcloud.py to link each word to all the lines that contain it.
For example, when you click on a word, it should display all the lines where the word occurs. 

--- linked_cloud.py
 
7) Create new files and Change 3-4-5-6 to create bigram cloud (pairs of words) instead of single word cloud.
		
	move to bigrams folder -
	cd bigrams 
	python filename.py

		In the bigrams folder -- 
		3 )  -- word_freq_bigrams.py
		4 )  -- word_freq_bigrams_noise_words_removed
		5 )  -- tag_cloud_bigrams.py
		6 )  -- linkedcloud_bigrams.py




 
Create a git repo, upload these tasks as you finish each task and send the url of that repo.
 

