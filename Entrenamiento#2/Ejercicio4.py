#LEFT AND RIGHT ARRAY 1

""" Camilo necesita un poco de ayuda con la tarea que le da su maestra.
La tarea consiste en multiplicar la suma de la primera mitad por la suma de la segunda
mitad de un vector de N posiciones.

Formato de entrada

La primera línea consta de casos de prueba T. Cada línea de caso de prueba consta
de un número entero N correspondiente al tamaño del vector y en la otra línea
consta de Ai que son cada uno de los elementos del vector.

Restricciones

1≤T≤100
1≤N≤1000
1 ≤ Ai ≤ 100

Formato de salida

Imprime el resultado esperado multiplicando las dos sumas de cada mitad del vector.

Entrada de muestra 0

2
5
2 3 4 5 6
4
1 2 3 4
Salida de muestra 0

55
21
Explicación 0

En el primer vector, el número de posiciones es impar, por lo que se suman los elementos
a la izquierda de la posición central (2 + 3 = 5), y luego se suman los elementos
a la derecha de la posición central (5 + 6 = 11). Al multiplicar estas dos sumas
el resultado a imprimir es 55.
En el segundo vector, el número de posiciones es par,
por lo que se suman los elementos de la izquierda (1 + 2 = 3),
y luego se suman los elementos del lado derecho (3 + 4 = 7).
Al multiplicar estas dos sumas, el resultado a imprimir es 21. """

T=int(input())
for i in range(T):
    N=int(input())
    ai=list(map(int, input().split()))
    SUMA_DER=0
    SUMA_IZQ=0
    for i in range(N//2):
        SUMA_IZQ+=ai[i]
        SUMA_DER+=ai[N-i-1]
    print(SUMA_DER*SUMA_IZQ)