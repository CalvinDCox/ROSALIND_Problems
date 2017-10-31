#Evolution as a Sequence of Mistake
#Calvin D. Cox
#10/30/2017

#Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t)dH(s,t).

#A little upset this one is so simple compared to the Counting GC content one
#Readfile
file = open('exampletext.txt')
strains = file.readlines()

#since we know what the input looks like we will insert the sequences into two separate variables right out
dna1 = strains[0].rstrip("\n")
dna2 = strains[1].rstrip("\n")

#Declaring the important part that holds the Hamming Distance
count = 0

#Loops through both sequences, this only works if they are the same length though.
for i,j in zip(dna1,dna2):
    if i != j:
        count += 1

#Print Hamming Distance        
print(count)
