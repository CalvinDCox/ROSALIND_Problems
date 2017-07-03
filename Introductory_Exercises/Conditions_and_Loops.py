#Conditions and Loops

#http://rosalind.info/problems/ini4/
#Given: Two positive integers aa and bb (a<b<10000a<b<10000).
#Return: The sum of all odd integers from aa through bb, inclusively.


#Reading two lines from input file
with open('rosalind_ini3.txt','r') as file:
    cache = file.readline()
    
#converting extracted 4 numbers to ints
split = str.split(cache)
coord = list(map(int, split))

#declare for loop
count = coord[0]
end = coord[1]
sum_of_all = 0

#for loop to add numbers within range (inclusive)
while (count <= end):
    if (count % 2 == 0):  
        pass
    else: 
        sum_of_all = sum_of_all + count
    count += 1
    
print(sum_of_all)
