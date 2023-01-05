#ELIMINACIÓN MÁXIMA Y MÍNIMA
""" En algunas prácticas estadísticas se recomienda eliminar el valor máximo y el valor mínimo de una serie de datos (se eliminan ambos extremos para evitar o disminuir la desviación o el sesgo en esos datos). En este nuevo reto se pide “quitar” el máximo y el mínimo de T cantidad de vectores sin afectar su orden original.

Input Format

En la primera línea se lee un número entero T que corresponde al número total de casos. Cada caso de prueba tiene dos nuevas líneas: una donde se lee un número entero N que corresponde al tamaño del vector y en la siguiente línea se lee cada uno de los elementos (ai) del vector.

Constraints

1 ≤ T ≤ 20
1 ≤ N ≤ 100
1 ≤ ai ≤ 100000

Output Format

Por cada caso de prueba imprimir un mensaje que indique el caso actual, seguido de dos puntos (:), terminando con los elementos del arreglo encerrados en corchetes y separados por espacio (sin incluir el máximo y el mínimo). Dejar un espacio después del corchete que abre y antes del corchete que cierra. Ver los ejemplos y sus explicaciones.

Sample Input 0

1
5
2 8 7 9 1
Sample Output 0

Caso 1: [ 2 8 7 ]
Explanation 0

En este vector [2 8 7 9 1] se elimina el #9 (máximo) y el #1 (mínimo) quedando como resultado los elementos [ 2 8 7 ]. Se imprime Caso 1: [ 2 8 7 ].

Sample Input 1

2
8
53 25 76 59 87 85 45 10
4
75 97 45 32
Sample Output 1

Caso 1: [ 53 25 76 59 85 45 ]
Caso 2: [ 75 45 ]
Explanation 1

En este primer vector de este ejemplo [53 25 76 59 87 85 45 10] se elimina el #87 (máximo) y el #10 (mínimo) quedando como resultado los elementos [53 25 76 59 85 45]. Se imprime Caso 1: [ 53 25 76 59 85 45 ].
En el segundo vector de este ejemplo [75 97 45 32] se elimina el #97 (máximo) y el #32 (mínimo) quedando como resultado los elementos [75 45]. Se imprime Caso 2: [ 75 45 ].

Sample Input 2

1
4
6457 5479 5454 3128
Sample Output 2

Caso 1: [ 5479 5454 ]
Sample Input 3

4
8
67173 25007 67713 54809 79057 65167 47450 35137
5
1416 9982 9453 4369 5689
20
322 639 317 256 896 224 373 119 628 683 953 377 262 266 581 532 922 936 200 201
8
79 456 21 230 87 734 371 194
Sample Output 3

Caso 1: [ 67173 67713 54809 65167 47450 35137 ]
Caso 2: [ 9453 4369 5689 ]
Caso 3: [ 322 639 317 256 896 224 373 628 683 377 262 266 581 532 922 936 200 201 ]
Caso 4: [ 79 456 230 87 371 194 ] """

""" T=int(input())
for i in range(T):
    N=int(input())
    vector=list(map(int, input().split()))
    maximo=vector[0]
    minimo=vector[0]
    for j in range(1, N-1):
        if (maximo<vector[j]):
            maximo=vector[j]
        else:
            maximo+=0
    for j in range(1, N-1):
        if (minimo>vector[j]):
            minimo=vector[j]
        else:
            minimo+=0
    vector.remove(maximo)
    vector.remove(min)
    print("caso {0}: [{1}]".format(i, *vector))  """









#Esta bien pero no se imprime como lo pide el juez 
T=int(input())
for i in range(T):
    N=int(input())
    vector=list(map(int, input().split()))
    maximo=max(vector)
    minimo=min(vector) 
    vector.remove(maximo) 
    vector.remove(minimo)

