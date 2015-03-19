#Extracting text and tracing the most frequent words and association with failures
#NLP usage for determining the failures of the industrial plant
import string
import nltk
from nltk import FreqDist
#import scipy
import numpy

import csv
path="C:\Users\Chandra\Documents\iGate\NLP\\"
file=open(path+"fire-inspection-findings1.csv")
data = csv.reader(file)
# reading headers of the file
headers = data.next()

print headers
#creating columns with the headers names
column = {}
for h in headers:
    column[h]=[]
    
print column
#saving the column data in the
for row in data:
    for h, v in zip(headers, row):
        column[h].append(v)
#print the values in the columns up to 5 rows!
print column['Title'][1:5] 

all_words=[]
count = 0
#copying all the text in to one set all_words
for site in column['Site']:
    print site
    count=count+1
    if count>10: 
       break


    
# for titles in column['Title']:
    # print count
    # print titles.split()
    # all_words.append(titles.split())

    # # count=count+1
    # # if count>30: 
       # # break

# print "All_words"
# print all_words
# # creating flatten set
# All_words_flatten=[words for elem in all_words for words in elem]
# # converting to upper case to easy sort and count
# All_words_Ucase=[words.upper() for words in All_words_flatten]
# All_words_f_sort=sorted(All_words_Ucase)

# # print All_words_flatten
# # print "Sort"
# # print All_words_f_sort 
   
# #print len(All_words_flatten)    
# print len(All_words_f_sort)
# print All_words_f_sort.count("THE")
# # unique set and length of words from list of words
# print set(All_words_f_sort)
# print len(set(All_words_f_sort))

# # source from nltk.org/book
# # gives the diversity in the list:  ((unique set)/ (all words count))
# def lexical_diversity(text):
    # return float(len(set(text))) / float(len(text))
# # gives the percentage    
# def percentage(count, total):
    # return 100 * float(count) / total
    
# print lexical_diversity(All_words_f_sort)
# print percentage(All_words_f_sort.count("FAILURE"),len(All_words_f_sort))

# #getting distribution of words. Could also used counters from collections!
# fdist=FreqDist(All_words_f_sort)

# #top 20 of most occurrence words
# top_words = fdist.most_common(20)
# #print(top_words)
# with open(path+"words_count.csv", "wb") as fp:
    # writer = csv.writer(fp, delimiter=',')
    # writer.writerows(top_words)
# # occurrence of word "FAILURE"
# # print fdist["FAILURE"]

# #plot cumulative count with top 20 words
# #fdist.plot(20, cumulative=True)





       
