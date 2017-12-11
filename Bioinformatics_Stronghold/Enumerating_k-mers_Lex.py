#Enumerating k-mers Lexicogrphically
#Calvin D. Cox
#12/10/2017

#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10n≤10).
#Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

from itertools import product as prod
import re

#Loading in the Sequence Files
with open('exampletext.txt', 'r') as et:
    data_set = et.readlines()

#Store permutation in an acceptable format to be sorted
perm_store = []
num_perm = prod(re.sub("[^A-Z]", "", data_set[0]), repeat=int(re.sub("[^1-9]", "", data_set[1])))
for i in list(num_perm):
    perm_store.append(re.sub("[^A-Z]", "", str(i)))
    
#Sort permutation list
## BUG seems to not want to not repeats.
sorted(perm_store)

with open('resulttext.txt', 'w') as rt:
    for i in perm_store:
        rt.write(i + '\n')
    
