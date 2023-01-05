#MATRIX INTERCHANGE 1
"""Trabajar con matrices 2D es bastante importante. Aquí haremos el intercambio de columnas en una matriz 2D. Se le da una matriz M de R filas y C columnas. Su tarea es intercambiar la información en las columnas de la matriz. Intercambia el primero con el último, el segundo con el penúltimo, y así sucesivamente con los demás.

Formato de entrada

La primera línea de entrada contiene T, el número de casos de prueba. Cada testcase contiene dos líneas de entrada. La primera línea contiene R y C, separados por un espacio. Las siguientes líneas contienen elementos enteros de la matriz, separados por espacios.

Restricciones

1 ≤ T ≤ 100
1 ≤ R, C ≤ 100

Formato de salida

Para cada caso de prueba, en una nueva línea, imprima la matriz modificada.

Entrada de muestra 0

1
3 5
1 2 10 3 4
4 3 11 2 1
6 7 12 8 9
Salida de muestra 0

4 3 10 2 1
1 2 11 3 4
9 8 12 7 6
Explicación 0

En este ejemplo, la primera columna se intercambia con la quinta y la segunda con la cuarta. La tercera columna permanece intacta en matrices con número impar de columnas. """

T=int(input())
for veces in range(T):
    R, C= map(int, input().split())
    matriz=[]
    for i in range(R):
        matriz.append(list(map(int, input().split())))
    for i in range(R):
        for j in range(C//2):
            aux=matriz[i][j]
            matriz[i][j]=matriz[i][C-j-1]
            matriz[i][C-j-1]=aux 
    for i in range(R):
        for j in range(C):
            print(matriz[i][j], end=" ")
        print("")
