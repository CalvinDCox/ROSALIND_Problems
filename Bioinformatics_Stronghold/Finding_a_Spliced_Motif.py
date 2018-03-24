#Finding a Spliced Motif
#3/24/2018
#Calvin D. Cox

#open file and store it in a variable
with open('exampletext.txt') as file:
    fasta = file.readlines()
#This stores the entire set of fasta files as a list

#Now to split the files into a dict
listed = []
fastastore = {}
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
        listed.append(fasta[i].rstrip("\n"))
        fastastore[fasta[i].rstrip("\n")] = nuc
 
count = 0
ffirst = listed[0].rstrip("\n")
fsecond = listed[1].rstrip("\n")
pos_store = []
i = 0
m = 0

for j in fastastore[ffirst]:
    
    try:
        if j == fastastore[fsecond][i] and i <= len(fastastore[fsecond]):
            pos_store.append(m+1)
            i = i + 1
    except IndexError:
        pass
    m = m + 1
    
print(' '.join(str(h) for h in pos_store))
