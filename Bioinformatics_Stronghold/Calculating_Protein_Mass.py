#Calculating Protien Mass
#Calvin D. Cox
#12/07/2017

#Given: A protein string PP of length at most 1000 aa.
#Return: The total weight of PP. Consult the monoisotopic mass table.

import re

#Load Files
with open('exampletext.txt', 'r') as aa:
    P = aa.readline()
    
with open('Mono_pro.txt', 'r') as tf:
    pro_table = tf.readlines()

#Create a dictionary from the table, I cheated a bit and loaded the table from the site into a notepad file. 
aminos = {}    
for n in pro_table:
    aminos[n[0]] = float(re.sub("[^0123456789\.]", "", n.rstrip())) #much cleaner way to do this?

#Calculating mass
mass = 0    
P = P.rstrip()
for a in P:
    mass += aminos[a]
 
print(str(round(mass, 3)))
