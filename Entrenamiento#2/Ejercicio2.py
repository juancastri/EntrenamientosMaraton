#FRIENDS NUMBERS 1

""" Two friendly numbers are two positive integers ‘a’ and ‘b’ such that the sum of one's own
divisors is equal to the other number and viceversa.

An example of friendly numbers is the pair of natural numbers (220, 284),
such that the proper divisors of 220 that add up to 284 and the proper divisors of 284
that add up to 220. See the explanation of the example of the statement.

Based on this concept, a solution is required to create two vectors of N positions called ‘A’ and ‘B’.
Then go through both arrangements and compare the two numbers of each position and print "Friend" or "Not friend"
depending on the case.

Input Format

The first input line contains T the number of test cases. 
The next line contains N being half the size of the vector,
the following line contains the numbers of vector A and the last line contains the numbers of vector B.

Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 10
1 ≤ Ai, Bi ≤ 10^8

Output Format

For each test case print "Friend" or "Not friend" depending on the case """

T=int(input())
for casos in range(T):
    N=int(input())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    for i in range(N):
        SUMA1=0
        for j in range(1,A[i]//2+1):
            if A[i] % j == 0:
                SUMA1+=j
        if SUMA1 == B[i]:
            SUMA2=0
            for j in range(1, B[i]//2+1):
                if B[i] % j == 0:
                    SUMA2+=j
            if SUMA2 == A[i]:
                print("Friend")
            else:
                print("Not friend")
        else:
                print("Not friend")