#Extracting text and tracing the most frequent words and association with failures
#NLP usage for determining the failures of the industrial plant
import string
import nltk
from nltk import FreqDist
import scipy
import numpy
import operator
from operator import itemgetter, attrgetter
#from itertools import groupby
import toolz
from toolz import groupby
import csv
from pandas import DataFrame
from pandas import groupby
#from pandas import groups

sevarity_score=[['SHUT DOWN',10],['FAILURE',10],['EMERGENCY',9],['INADEQUATE',8]]
#extra backward slash to get the path right
path="C:\Users\Chandra\Documents\iGate\NLP\\"
file=open(path+"fire-inspection-findings3.csv")
data = csv.reader(file)
# reading headers of the file
headers = data.next()
data_wo_headers=list(data)  # skip the headers
#sorted by site name alphabetically
sortedlist = sorted(data_wo_headers, key=operator.itemgetter(1), reverse=True)

print headers
print " "
print data_wo_headers
print " "
print sortedlist

#creating columns with the headers names
column = {}
column_wo_h={}

for h in headers:
    column[h]=[]
    
print column

column['Title_split']=[]
#saving the column data in tuple format
for row in sortedlist:
    for h, v in zip(headers, row): # can be improved by itertools.izip
        column[h].append(v)
        if h=='Title':
            print 1
            print v
            titles_up=v.upper()
            titles_sort=sorted(titles_up.split())
            column['Title_split'].append(titles_sort)
    
#print the values in the columns up to 5 rows!
#print column['Title'][1:5] 
print column
print "Data Frame"
DF_column=DataFrame(column)
print DF_column
print column['Site']
print DF_column[DF_column['Site']=='CNS']
grouped= DF_column.groupby('Site')
# grouped= groupby(column('Site'),column)
print "Groups"


for name, group in grouped:
    print name
    print group
    DF_columngrp=Dataframe(group)
    DF_columngrp.toCSV(path+"test1_4.csv", sep='\t')
print "w/o for groups"
print grouped.groups

# with open(path+"test1_4.csv", "wb") as fp:
    # writer = csv.writer(fp, delimiter=',')
    # for name, group in grouped:
        # print name
        # print group
        # DF_columngrp=Dataframe(group)
        # writer.writerow(name)
        # writer.writerow(group)
    
# print column

# all_words=[]
# count = 0
# column['Title_split']=[]
# # #copying all the text in to one set all_words
# for titles in column['Title']:
    # #print count
    # #print titles.split()
    # titles_up=titles.upper()
    # titles_sort=sorted(titles_up.split())
    # all_words.append(titles.split())
    # column['Title_split'].append(titles_sort)

    # # count=count+1
    # # # if count>30: 
       # # # break
# print "All_words"
# print column

# with open(path+"test1_3.csv", "wb") as fp:
    # writer = csv.writer(fp, delimiter=',')
    # writer.writerows(sortedlist)
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
# print(fdist)

# #prints top 10 of most occurrence words
# top10 = fdist.most_common(10)
# print(top10)

# occurrence of word "FAILURE"
#print fdist["FAILURE"]

#plot cumulative count with top 20 words
#fdist.plot(20, cumulative=True)



       
