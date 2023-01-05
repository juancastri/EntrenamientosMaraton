#THE NATIONAL ARTS SKILLS 1

""" Los resultados obtenidos por los participantes del maratón nacional de matemáticas y lenguaje
se almacenan en un vector de dimensión N. Las puntuaciones de matemáticas se almacenan en posiciones
pares y las puntuaciones de lenguaje en posiciones impares. Cada año Carlos tiene la tarea
de presentar el informe de qué habilidad obtuvo el mejor resultado.
Tu tarea es encontrar el puntaje más alto en matemáticas y el puntaje más alto en lenguaje.
Dependiendo de estos valores, debe imprimir:

• 1 si la puntuación máxima en matemáticas es superior a la puntuación máxima en lengua
• -1 si la puntuación máxima en matemáticas es inferior a la puntuación máxima en lenguaje.
• 0 si la puntuación máxima en matemáticas es igual a la puntuación máxima en lengua

Formato de entrada

La primera línea de entrada contiene T el número de casos de prueba.
La siguiente línea contiene N siendo la mitad del tamaño del vector,
las siguientes líneas contienen los puntajes de las pruebas de lenguaje y matemáticas separados por un solo espacio.

Restricciones

1 ≤ T ≤ 100
1 ≤ norte ≤ 80
0 ≤ puntuación ≤ 100

Formato de salida

Para cada caso de prueba, imprima los valores resultantes (1, 0 o -1).

Entrada de muestra 0

1
10
4 11 6 93 69 80 34 63 48 62

Salida de muestra 0

-1
Explicación 0

La puntuación máxima en matemáticas es 69 (Posición 4) y la puntuación máxima en lenguaje es 93 (Posición 3),
por lo que se imprime -1, porque la puntuación máxima en matemáticas es inferior 
a la puntuación máxima en lenguaje. """

T=int(input())
for casos in range(T):
    N=int(input())
    puntuacion=list(map(int, input().split()))
    MAX_MAT=0
    MAX_LEN=0
    for i in range(1, N, 2):
        print(puntuacion[i])
        """ if (puntuacion[i]>MAX_LEN):
            MAX_LEN=puntuacion[i]
        if(puntuacion[i-1]>MAX_MAT):
            MAX_MAT=puntuacion[i-1]
    if (MAX_MAT > MAX_LEN):
        print("1")
    elif (MAX_MAT < MAX_LEN):
        print("-1")
    else:
        print("0") """
