#Enumerating_Oriented_Gene_Orderings
#Calvin D. Cox
#12/10/2017

#Given: A positive integer n≤6n≤6.
#Return: The total number of signed permutations of length nn, followed by a list of all such permutations (you may list the signed permutations in any order).

from itertools import permutations as perm
import re
import collections

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
num_perm = perm(ini_mirror, int(data_set))
for i in list(num_perm):
    ik = re.sub("[^\d+$]", "", str(i))
    if len(set(ik)) == len(ik):
        perm_store.append(re.sub("[^-\d+$ ]", "", str(i)))
    
with open('resulttext.txt', 'w') as rt:
    rt.write(str(len(perm_store)) + '\n')
    for i in perm_store:
       rt.write(i + '\n')
  
