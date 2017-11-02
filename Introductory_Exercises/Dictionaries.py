#Intro to Python Dictionary
#Calvin D. Cox
#11/01/2017

#Given: A string ss of length at most 10000 letters.
#Return: The number of occurrences of each word in ss, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

file = open('exampletext.txt')
words = file.readline()

words = words.rstrip("\n")
words = words.split(' ')
worddict = {}


for i in words:
    if i in worddict:
        worddict[i] += 1
    else:
        worddict[i] = 1
        
for key, value in worddict.items():
    print (str(key) + ' ' + str(value))
