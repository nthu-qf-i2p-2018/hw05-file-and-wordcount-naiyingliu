
# coding: utf-8

# In[4]:


# -*- coding: utf-8 -*-
import string
import csv
import json
import pickle
from collections import Counter

def main(filename):
    # read file into lines
    lines = open(filename).readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip(string.punctuation)
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)
                
    # compute word count from all_words
    counter = Counter(all_words).most_common()
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('wordcount.csv','w',newline='') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(counter)
        

    # dump to a json file named "wordcount.json"
    #json_text = json.dumps(counter)
    with open('wordcount.json', 'w') as f:
        json.dump(counter, f)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    pickle.dump(counter, open("wordcount.pkl", 'wb'))
    
    # hint: dump the Counter object directly

    
if __name__ == '__main__':
    main("i_have_a_dream.txt")

