#Enumerating k-mers Lexicogrphically
#Calvin D. Cox
#12/10/2017

#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10n≤10).
#Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

from itertools import product as prod
import re

#Loading in the Sequence Files
with open('exampletext.txt', 'r') as et:
    data_set = et.readline()

#Create chart with all possible permutations 
i = 1
ini_mirror = []
while i <= int(data_set):
    ini_mirror.append(int(i))
    ini_mirror.append(-int(i))
    i += 1
    

#Store permutation in an acceptable format to be sorted
perm_store = []
num_perm = prod(ini_mirror, repeat=int(data_set))
for i in list(num_perm):
    perm_store.append(re.sub("[^-\d+$]", "", str(i)))
    
with open('resulttext.txt', 'w') as rt:
    for i in perm_store:
        print(i)
        rt.write(i + '\n')
  
