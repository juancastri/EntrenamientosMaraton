#TABLERO DE AJEDREZ 1
""" En este nuevo reto te dan una matriz de orden N simulando un tablero de ajedrez como el de la imagen.
image

Debes imprimir la diferencia entre la sumatoria de las casillas de color blanco con la sumatoria de las
casillas de color negro.

Input Format

La primera línea contiene un número entero T que indica el número de casos de prueba.
Cada caso de prueba consta de dos líneas, la primera línea de cada caso de prueba contiene
un número N entero que indica el orden de la Matriz y la segunda línea contiene los elementos (Matriz[i][j])
separados por espacios.

Constraints

1 ≤ T ≤ 100
4 ≤ N ≤ 100
0 ≤ Matriz[i][j] ≤ 100

Output Format

La salida, para cada caso de prueba, en una nueva línea imprima la diferencia entre el valor acumulado
entre las casillas blancas y las negras.

Sample Input 0

1
6
4 3 3 3 5 4
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
0 2 0 4 5 1
Sample Output 0

4
Explanation 0

En este primer ejemplo, sumamos los valores de las casillas de ambos colores:
suma de casillas blancas es igual a 61 (4 + 3 + 5 + 2 + 4 + 6 + 1 + 3 + 5 + 2 + 4 + 6 + 1 + 3 + 5 + 2 + 4 + 1)
y la suma de las casillas negras es igual a 57 (3 + 3 + 4 + 1 + 3 + 5 + 2 + 4 + 6 + 1 + 3 + 5 + 2 + 4 + 6 + 0 + 0 + 5)
y su diferencia es igual a 4 (blancas = 61 - negras = 57).

Sample Input 1

1
4
4 1 2 3
4 5 2 3
1 9 4 9
0 2 1 3
Sample Output 1

-5
Explanation 1

En este segundo ejemplo, sumamos los valores de las casillas de ambos colores:
suma de casillas blancas es igual a 24 (4 + 2 + 5 + 3 + 1 + 4 + 2 + 3)
y la suma de las casillas negras es igual a 29 (1 + 3 + 4 + 2 + 9 + 9 + 0 + 1)
y su diferencia es igual a -5 (blancas = 24 - negras = 29).

Sample Input 2

1
5
11 12 13 14 14
98 22 12 44 11
84 88 22 33 77 
90 12 34 43 22
87 88 11 12 33
Sample Output 2

-41
Sample Input 3

2
6
12 3 4 2 4 5 
9 2 3 4 1 2
4 2 8 9 1 2
4 22 3 41 4 5
8 1 2 3 4 7
19 2 3 4 7 8
4
3 4 1 2 
4 5 2 3
4 3 2 4
1 7 4 5
Sample Output 3

50
6 """
T=int(input())
for veces in range(T):
    N=int(input())
    matriz=[list(map(int, input().split())) for j in range(N)]
    suma_blancas=0
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            suma_blancas+=matriz[i][j]
    for i in range(1, N, 2):
        for j in range(1, N, 2):
            suma_blancas+=matriz[i][j]
    suma_negras=0
    for i in range(0,N,2):
        for j in range(1,N,2):
            suma_negras+=matriz[i][j]
    for i in range(1,N,2):
        for j in range(0,N,2):
            suma_negras+=matriz[i][j]
    diferencia=suma_blancas - suma_negras
    print(diferencia)