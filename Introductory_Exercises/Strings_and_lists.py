#Strings and Lists

#http://rosalind.info/problems/ini3/
#Given: A string ss of length at most 200 letters and four integers aa, bb, cc and dd.
#Return: The slice of this string from indices aa through bb and cc through dd (with space in between), inclusively. In other words, we should include elements s[b]s[b] and s[d]s[d] in our slice.

#Declare
result = ""

#Reading two lines from input file
with open('rosalind_ini3.txt','r') as file:
    ss = file.readline()
    cache = file.readline()
    
#converting extracted 4 numbers to ints
split = str.split(cache)
coord = list(map(int, split))

#pulling out relevant characters from string
for i in range(coord[0], coord[1]):
 result += ss[i]

result += " "

#pulling out numbers for second range
for i in range(coord[2], coord[3]):
 result += ss[i]

#Show Result
print(result)
