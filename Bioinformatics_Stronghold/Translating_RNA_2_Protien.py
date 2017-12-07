#Translating RNA into Protein
#Calvin D. Cox
#11/30/2017

#Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).
#Return: The protein string encoded by ss.

#Loading MRNA
with open('exampletext.txt', 'r') as r:
    rna = r.readline()
#created a file for the rna codon table to make it searchable
with open('rna2pro.txt', 'r') as f:
    fan = f.readlines()
    aatable = ''.join(fan)

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

#Print result to file
with open('resulttest.txt', 'w') as result:
    result.write(amino)
