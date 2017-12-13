#Calvin D. Cox
#Finding a Motif in DNA
#12/12/2017

#Given: Two DNA strings ss and tt (each of length at most 1 kbp).
#Return: All locations of tt as a substring of ss.

import re

with open('exampletext.txt', 'r') as et:
    data_set = et.readlines()
    
dna = data_set[0]
primer = data_set[1]

matches = []
i = 0

while i < len(dna):
    if dna[i:i+len(primer)] == primer:
        matches.append(i+1)
    i += 1
    
print(re.sub("[^-\d+$ ]", "", str(matches)))