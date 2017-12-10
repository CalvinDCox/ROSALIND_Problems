#Enumerating k-mers Lexicogrphically
#Calvin D. Cox
#12/10/2017

#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n≤10n≤10).
#Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

from itertools import permutations as perm
import re

#Loading in the Sequence Files
with open('exampletext.txt', 'r') as et:
    data_set = et.readlines()

perm_store = []
num_perm = perm(re.sub("[^A-Z]", "", data_set[0]), int(data_set[1]))
for i in list(num_perm):
    perm_store.append(re.sub("[^A-Z]", "", str(i)))

