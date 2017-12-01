#Computing GC Content
#Calvin D. Cox
#10/29/2017

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

#open file and store it in a variable
file = open('exampletext.txt')
fasta = file.readlines()
#This stores the entire set of fasta files as a list

#Now to split the files into a managable format
nuc = ""
fastastore = {}
for i in range(0, len(fasta)):
    if ">" in fasta[i]:
        k = 1
        try:
            while ">" not in fasta[i+k]:
                    nuc  += fasta[i+k].rstrip("\n")
                    k += 1
        except IndexError:
            pass
        fastastore[fasta[i].rstrip("\n")] = nuc
 
#Calculate the File with the highest GC Content
winner = ""
winnergc = 0
 
for key, value in fastastore.items():
    AT = 0
    CG = 0
    
    for i in value:
        if i == "A":
            AT += 1
        elif i == "T":
            AT += 1
        elif i == "G":
            CG += 1
        elif i == "C":
            CG += 1
            
    gccontent = CG / (AT+CG)
    
    if gccontent > winnergc:
        winner = key
        winnergc = gccontent * 100

#Print the Winners
print(winner.replace(">", ""))
print(str(winnergc))