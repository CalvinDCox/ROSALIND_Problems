#RNA_Splicing
#Calvin D. Cox
#12/17/2017

#Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)

import string

#open file and store it in a variable
with open('exampletext.txt') as file:
    fasta = file.readlines()
#This stores the entire set of fasta files as a list

#Adding Translation Table to make later part in problem easier
with open('rna2pro.txt', 'r') as f:
    fan = f.readlines()
    aatable = ''.join(fan)

#Now to split the files into a dict

fastastore = {}
masterstore = {}
for i in range(0, len(fasta)):
    if ">" in fasta[i]:
        k = 1 #Resets k for next set of nucs
        nuc = "" #Resets nuc for next dictionary input
        try:
            while ">" not in fasta[i+k]:
                    nuc  += fasta[i+k].rstrip("\n")
                    k += 1
        except IndexError:
            pass
        if i == 0:
            masterstore['One'] = nuc
        else:    
            fastastore[fasta[i].rstrip("\n")] = nuc

#We now have our files and howmany ever splices the program throws at us.


ss =  masterstore['One']
#Pulling splices out of string one by one, the loop allows for an unlimited number of arguments.
for key, value in fastastore.items():
    ss = ss.replace(str(value), '')

#Converting the nucs to RNA for translation
def transcribe(nuc):
    if nuc == 'A':
        return 'A'
    elif nuc == 'C':
        return 'C'
    elif nuc == 'G':
        return 'G'
    elif nuc == 'T':
        return 'U'

#create bin for result 
rna = ''

for i in ss:
  rna = rna + transcribe(i)

#Translation to Protien
amino = ''
#Looped through the RNA by 3's
for nuc in range(3, len(rna), 3):
    #Nature is the best example.
    trna = rna[nuc-3:nuc]
    #Based on question design there was a stop codon at the end of every file, never in the middle. I figured I'd still put this here.
    if trna == 'UAG' or trna ==  'UAG' or trna == 'UGA':
        break
    else:
        aa = aatable.find(trna, 0) + 4
        amino += aatable[aa]

#Display protien for input
print(amino)