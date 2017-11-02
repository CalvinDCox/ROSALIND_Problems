#Intro to Python Dictionary
#Calvin D. Cox
#11/01/2017

#Given: A string ss of length at most 10000 letters.
#Return: The number of occurrences of each word in ss, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

#Pull line with words from file
file = open('exampletext.txt')
words = file.readline()

#Clean the file of newlines and then split by spaces
words = words.rstrip("\n")
words = words.split(' ')

#Create a dictionary to store the values in
worddict = {}

#Loop to check for keys, if the key is not found in the dictionary, then a new key is created. If it is already in the dictionary, then the total in the value column is updated.
for i in words:
    if i in worddict:
        worddict[i] += 1
    else:
        worddict[i] = 1

#Print result for outputs
for key, value in worddict.items():
    print (str(key) + ' ' + str(value))
