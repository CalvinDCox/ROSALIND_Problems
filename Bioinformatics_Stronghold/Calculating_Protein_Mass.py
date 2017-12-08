#Calculating Protien Mass
#Calvin D. Cox
#12/07/2017

#Given: A protein string PP of length at most 1000 aa.
#Return: The total weight of PP. Consult the monoisotopic mass table.
import re

with open('exampletext.txt', 'r') as aa:
    P = aa.readline()
    
with open('Mono_pro.txt', 'r') as tf:
    pro_table = tf.readlines()
    
mass = 0    
    
for a in P:
    for amino in pro_table:
        if a in amino:
            mass += float(re.sub("[^0123456789\.]", "", amino)) 
        
            
            