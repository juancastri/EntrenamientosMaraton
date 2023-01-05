#PROBLEMAS DIAGONALES

""" Los hermanos Diagonal tienen un problema y los dos se impusieron un reto: el que tenga mayor valor acumulado es el ganador y para eso necesitan de tu ayuda, ¿puedes ayudar a resolver este problema entre hermanos? Te dan una matriz de orden N par y tu tarea es hallar las sumatorias de ambas diagonales e imprimir: 1 si la suma de la diagonal principal es mayor. 2 si la suma de la diagonal secundaria es mayor y 3 si ambas sumas son iguales.

Input Format

La primera línea de entrada consta de un valor N, que indica el orden de la matriz y la segunda línea consta de N elementos separados por espacios.

Constraints

3 ≤ N ≤ 100
0 ≤ Matriz[i][j] ≤ 1000

Output Format

La salida consta que en una sola línea ponga: 1 si la suma de la diagonal principal es mayor. 2 si la suma de la diagonal secundaria es mayor y 3 si ambas son iguales.

Sample Input 0

3
1 2 3
4 5 6
7 8 9
Sample Output 0

3
Explanation 0

La suma de la diagonal principal es: 1 + 5 + 9 = 15, la suma de la diagonal secundaria es: 7 + 5 + 3 = 15, ambas sumas diagonales son iguales, por lo tanto, se imprime 3.

Sample Input 1

4
1 2 3 4
1 2 3 4
9 8 7 6
9 8 7 6
Sample Output 1

2
Explanation 1

La suma de la diagonal principal es: 1 + 2 + 7 + 6 = 16, la suma de la diagonal secundaria es: 9 + 8 + 3 + 4 = 24, al ser mayor la suma de la diagonal secundaria se imprime 2.

Sample Input 2

6
1 2 3 4 3 4
1 2 3 4 5 6 
9 8 7 6 7 8
9 8 7 6 9 10
4 4 4 4 4 4
6 7 8 9 1 2
Sample Output 2

2
Sample Input 3

5
1 5 9 7 6 
4 8 6 2 3
1 4 7 8 9
0 2 5 8 9 
4 6 3 1 5
Sample Output 3

1 """
N=int(input())
matriz=[]
diagonal_principal=0
diagonal_secundaria=0
j=-1
for i in range(N):
    matriz.append(list(map(int, input().split())))
for i in range(len(matriz)):
    diagonal_principal+=matriz[i][i]
for i in range(len(matriz)):
    diagonal_secundaria+=matriz[i][j]
    j=j-1
if(diagonal_principal>diagonal_secundaria):
    print("1")
elif(diagonal_secundaria>diagonal_principal):
    print("2")
else:
    print("3")
