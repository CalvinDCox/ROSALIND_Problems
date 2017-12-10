#Enumerating Gene Orders
#Calvin D. Cox
#12/10/17

from itertools import permutations as perm
import re

#Given: A positive integer n≤7n≤7.
#Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).

#Open File with Number
with open('exampletext.txt', 'r') as f:
    number = int(f.readline())

#Creating a populated list for the permutations program
numlist = []
i = 1
while i <= number:
    numlist.append(i)
    i += 1

#Creating permutation File, working with num_perm later in the printing process didn't work so I immediately put it into a workable list
perm_store = []
num_perm = perm(numlist, number)
for i in list(num_perm):
    perm_store.append(i)


length_perm = len(perm_store)

#Plugging results into file, while I was testing other numbers I noticed the permutations can get quite large so I opted to write things into a file.
with open('resulttext.txt', 'w') as rt:
    rt.write(str(length_perm)+'\n')
    for j in perm_store:
        rt.write(re.sub("[^0-9 ]", "", str(j)) + '\n') #Strips everything but spaces and numbers


    
    
