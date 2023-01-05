"""Write a program that reads a number T and fill a vector N[1000]
 with the numbers from 0 to T-1 repeated times, like as the example below.

Input
The input contains an integer number T (2 ≤ T ≤ 50).

Output
For each position of the array N, print "N[i] = x",
 where i is the array position and x is the number stored in that position. """

N = []
T=int(input())
for i in range(1000):
    C = 0
    while C < T:
        N.append(C)
        C += 1
    print('N[{0}] = {1}'.format(i,N[i])) 

