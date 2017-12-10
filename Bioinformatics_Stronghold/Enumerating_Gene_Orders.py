#Enumerating Gene Orders
#Calvin D. Cox
#12/10/17

from itertools import permutations as perm

#Given: A positive integer n≤7n≤7.
#Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).

#Open File with Number
with open('exampletext.txt', 'r') as f:
    number = int(f.readline())
 
numlist = []
i = 1
while i <= number:
    numlist.append(i)
    i += 1
    
num_perm = perm(numlist, number)
length_perm = len(list(num_perm))


print(len(list(num_perm)))

for i in list(num_perm):
    print(i)
    
    