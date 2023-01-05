#DIFERENCIA MÍNIMA (WARM UP)
""" Una secuencia de N enteros se denomina "Minimum Difference" 
si los valores absolutos de las diferencias entre elementos sucesivos toman todos los valores 
posibles del 1 a N - 1. Escribe un programa para determinar si cada secuencia de números
"Minimum Difference" o "Not Minimum Difference". Ver ejemplos para entender mejor el reto.

Input Format

Cada línea de entrada contiene un número entero N, que corresponde a la dimensión del vector
y finalmente, se lee cada uno de sus elementos (ai).

Constraints

1 ≤ N ≤ 100
1 ≤ ai ≤ 1000

Output Format

Para cada vector genere una línea de salida que imprima 0 si es "Minimum Difference"
 o 1 si es "Not Minimum Difference".

Sample Input 0

4
1 4 2 3
Sample Output 0

0
Explanation 0

En el primer ejemplo se imprime 0, porque las diferencias absolutas de la secuencia
son 3, 2 y 1, respectivamente. Todas están entre 1 y 3 (N-1), incluyendo los extremos.

Sample Input 1

6
4 2 15 8 6 20
Sample Output 1

1
Explanation 1

En el segundo ejemplo se imprime 1, porque las diferencias absolutas de la secuencia son 
2, 13, 7, 2 y 14, respectivamente. Las diferencias 13 y 14 no están entre 1 y 5 (N-1). """

""" N=int(input())
elementos=list(map(int, input().split()))
suma=0
for i in range(N-1):
    for j in range(i+1, N):
        resta=abs(elementos[i]-elementos[j])
        if resta < N:
            suma+=0
        else:
            suma+=1
if suma == 0:
    print("0")
else:
    print("1") """

#RESPUESTA CORRECTA
N=int(input())
elementos=list(map(int, input().split()))
minium_diference=0
for i in range(1, N-1):
    diferencia=abs(elementos[i]-elementos[i-1])
    if (diferencia <= N-1):
        minium_diference+=0
    else:
        minium_diference+=1
if (minium_diference == 0):
    print("0")
else:
    print("1")
