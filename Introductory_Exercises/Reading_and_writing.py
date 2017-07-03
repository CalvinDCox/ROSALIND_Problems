#Reading and Writing

#http://rosalind.info/problems/ini5/
#Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.


cache =""
#Reading two lines from input file
with open('rosalind_ini3.txt','r') as f:
    count = 0
    for line in f:
        cache = line
        count += 1
        if count % 2 == 0:
            output = open('r_output.txt', 'a')
            output.write(cache)
    output = open('r_output.txt', 'a')
    output.write(cache)
    
