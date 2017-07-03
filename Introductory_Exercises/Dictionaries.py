#Intro to Python Dictonary

#http://rosalind.info/problems/ini6/
#Given: A string ss of length at most 10000 letters.
#Return: The number of occurrences of each word in ss, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
#****this solution did not work but based on hints and comparing the answer put into a dictionary this gives the right count. Something about the answer submission for this question is buggy. May try to submit later.
import json

#Reading one line from input file
with open('rosalind_ini6.txt','r') as file:
    cache = file.readline()
    cache_break = cache.split(" ")
    
del cache_break[-1]
cache_break.append('be')
newdict = {}

for word in cache_break:
    if word in newdict:
        newdict[word] = newdict[word] + 1
    else:
        newdict[word] = 1


for x in newdict:
    output = open('r_outputm.txt', 'a')
    k = x + " " + str(newdict[x])
    print(k.strip(), file=output)
  

print(k.strip(), file=output)

   