""" Teniendo N números en un vector A, se necesita saber si estos son PERFECTOS o IMPERFECTOS. Se imprime PERFECTO, si la sumatoria, de la potencia de cada elemento elevado a la posición+1, es múltiplo de la dimensión del vector (N); en caso contrario, se muestra IMPERFECTO.

Input Format

La primera línea consta de un entero N que corresponde a la dimensión del vector. Posteriormente cada ai números, son los elementos del vector que será manipulados por el programa.

Constraints

1 ≤ N ≤ 20
1 ≤ ai ≤ 100

Output Format

Se imprime 'PERFECTO', si el acumulado de la potencia del número elevado a la posición (esta posición es en base 1) que se encuentra el elemento es múltiplo de N; en caso contrario, se muestra 'IMPERFECTO'.

Sample Input 0

7
1 2 3 4 5 6 7
Sample Output 0

IMPERFECTO
Explanation 0

La sumatoria es igual a 873612 (1 ^ 1 + 2 ^ 2 + 3 ^ 3 + 4 ^ 4 + 5 ^ 5 + 6 ^ 6 + 7 ^ 7 = 1 + 4 + 27 + 256 + 3125 + 46656 + 823543), cuyo resultado no es múltiplo de N (7), por lo que se imprime IMPERFECTO.

Sample Input 1

4
31 97 12 16
Sample Output 1

PERFECTO
Explanation 1

La sumatoria es igual a 76704 (31 ^ 1 + 97 ^ 2 + 12 ^ 3 + 16 ^ 4 = 31 + 9409 + 1728 + 65536), cuyo resultado es múltiplo de N (4), por lo que se imprime PERFECTO. """
N=int(input()) #dimension del vector
elemento=list(map(int, input().split()))
contador=1
suma=0
for i in range(N):
    potencia = elemento[i]**contador
    suma+=potencia
    contador+=1
if(suma % N == 0):
    print("PERFECTO")
else:
    print("IMPERFECTO")