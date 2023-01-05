#MAGIC NUMBERS 9
""" In the Gotham City there is a magical company. His specialization is the creation of magical
algorithms to sell to different small businesses. Jairo, an American professor,
requested an algorithm that when entering a number that says if a number is magical or not.
It is known that magic numbers are those whose sum of their digits is even.

Input Format

The first line of input contains T, the number of testcases. T testcases follow.
Each test case contains an integer N denoting the number to read.

Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 10000

Output Format

For each test case, print “magical” if is a magical number or “not magical” if the number is not magical.

Sample Input 0

2
13
298
Sample Output 0

magical
not magical
Explanation 0

13 is a magical number because the sum of their digits 4 (1+3) is even, then print magical.
298 isn't magical number because the sum of their digits 19 (2+9+8) isn't even, then print not magical.

Sample Input 1

2
13
1000
Sample Output 1

magical
not magical """
T=int(input())
for veces in range(T):
    N=int(input())
    suma=0
    while (N > 0):
        suma+=N % 10
        N= N//10
    if (suma % 2 == 0):
        print("magical")
    else:
        print("not magical")
        
