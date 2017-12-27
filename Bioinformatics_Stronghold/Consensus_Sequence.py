#Consensus and Profile
#Calvin D. Cox
#12/19/2017

#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

#open file and store it in a variable
with open('exampletext.txt') as file:
    fasta = file.readlines()
#This stores the entire set of fasta files as a list

#Now to split the files into a dict

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
        fastastore[fasta[i].rstrip("\n")] = nuc
        
A, G, C, T = [], [], [], []       


for key, value in fastastore.items():
    a_cnt, g_cnt, c_cnt, t_cnt = 0, 0, 0, 0
    count = 0
    for mer in value:
        if mer == "A":
            a_cnt += 1
        elif mer == "G":
            g_cnt += 1
        elif mer == "C":
            c_cnt += 1
        elif mer == "T":
            t_cnt += 1
        count +=1
        
        A.append(a_cnt)
        G.append(g_cnt)
        C.append(c_cnt)
        T.append(t_cnt)

