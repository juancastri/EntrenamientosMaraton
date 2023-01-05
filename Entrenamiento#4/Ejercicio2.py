""" Carlos es aficionado al LoL pero es muy mal jugador, actualmente está en hierro IV y su única forma de salir de ese hueco es solucionando un ejercicio de programación. Tú serás el encargado de darle la solución y así llevarlo a la liga más alta del juego.
Para este reto te dan una matriz de tamañoMxNy tu tarea es imprimir esa matriz en forma de espiral. En la siguiente matriz se debería imprimir los valores: 82, 37, 25, 33, 75, 60, 86, 90, 64, 95, 68, 28, 70, 35, 87 y 40.

image

Formato de entrada

La primera línea de la entrada contiene un solo entero T, que denota el número de casos de prueba. Cada caso de prueba tiene dos líneas. La primera línea contiene M y N, separados por un espacio, que corresponden a la dimensión de la matriz. Las siguientes líneas son los valores de la matriz dividos por filas y columnas separados por un espacio en blanco.

Restricciones

1 ≤ T ≤ 100
2 ≤ M, N ≤ 10

Formato de salida

La salida a este reto, será una sola línea con los elementos de la matriz en forma de espiral.

Entrada de muestra 0

1
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Salida de muestra 0

1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explicación 0

La respuesta serán los números de la matriz, haciendo el recorrido en espiral: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Entrada de muestra 1

1 
3 4
9 3 2 4
5 8 1 9
2 3 4 5
Resultado de ejemplo 1

9 3 2 4 9 5 4 3 2 5 8 1
Explicación 1

La respuesta serán los números de la matriz, haciendo el recorrido en espiral:9 3 2 4 9 5 4 3 2 5 8 1 """

#pedir casos de prueba
from re import X


T=int(input())

#Dimension de la matriz
M, N=map(int, input().split())

#valores de la matriz
matriz=[list(map(int, input().split())) for i in range(M)]

#organizar los valore
x=0
y=0
i=0
limizq=0
limder=0
limsup=0
liminf=0
direccion=0

while(i<len(matriz)):
    matriz[x][y]= matriz[i]