#Consensus and Profile
#Calvin D. Cox
#12/19/2017



#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

import re

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

#Initiating Items in Loop      
A, G, C, T = [], [], [], []       
started = False

#Loop to go through all the nucs in each FASTA file
for key, value in fastastore.items():

    count = 0
    for mer in value:
        a_cnt, g_cnt, c_cnt, t_cnt = 0, 0, 0, 0 #Set here to reset for each go through of k-mer
        if mer == "A":
            a_cnt += 1
        elif mer == "G":
            g_cnt += 1
        elif mer == "C":
            c_cnt += 1
        elif mer == "T":
            t_cnt += 1
        count +=1
        if started == False:
            A.append(a_cnt)
            G.append(g_cnt)
            C.append(c_cnt)
            T.append(t_cnt)
            
        else:
            A[count-1] += a_cnt
            G[count-1] += g_cnt
            C[count-1] += c_cnt
            T[count-1] += t_cnt
    started = True

#Now that I have all the A's, C's, G's, T's stored its time to make the consensus sequence and display results.
consensus_sequence = []
for dd in range(len(A)):
    placeholder = A[dd]
    character = 'A'
    if C[dd] > placeholder:
        placeholder = C[dd]
        character = 'C'
    if G[dd] > placeholder:
        placeholder = G[dd]
        character = 'G'
    if T[dd] > placeholder:
        character = 'T'
    
    consensus_sequence.append(character)

#Have to organize output
with open('resulttext.txt', 'w') as rt:
    rt.write("".join(consensus_sequence) + '\n')
    rt.write("A: " + re.sub("[^0-9 ]", "", str(A)) + '\n')
    rt.write("C: " + re.sub("[^0-9 ]", "", str(C)) + '\n')
    rt.write("G: " + re.sub("[^0-9 ]", "", str(G)) + '\n')
    rt.write("T: " + re.sub("[^0-9 ]", "", str(T)) + '\n')
