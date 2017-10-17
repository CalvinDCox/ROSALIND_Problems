#Wascally Wabbits
#10/15/2017
#Calvin D. Cox

#Given: Positive integers n≤40n≤40 and k≤5k≤5.
#Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).
#For the sake of speed I decided to take out input and output stuff for the moment.

#Sample Dataset
n = 36
k = 2

#Creating the easy part of the sequence to make the loop easier.
pairs = [1,1]

#setting up sequence at right spot
i=3

#Sequence
while i <= n:
    x = pairs[-2]*k + pairs[-1] 
    pairs.append(x)
    i = i + 1
    
print(pairs)
