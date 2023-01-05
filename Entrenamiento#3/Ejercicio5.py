#BASE DE DATOS OG
""" ¿Recuerdas al cavernícola Og, aquel que no podía ni contar a sus hijos? El tiempo ha pasado y ahora está realizando encuestas sobre la longevidad de los seres humanos; para ello él llena manualmente todos los días una matriz con las edades de las personas encuestadas, pero le cuesta decir cuantas personas están por encima de la moda por cada uno de los días (cada fila de la matriz). Buscar el concepto estadístico de moda. Og te pide ayuda para crear una solución en la cual se muéstrela cantidad de personas que cumplen con el criterio antes mencionado, para continuar con sus cálculos estadísticos y así poder sacar sus conclusiones.

Input Format

La primera línea tiene dos números enteros positivos D y E separados por un espacio que corresponden al número de filas y el número de columnas de la matriz, respectivamente. Las siguientes líneas tienen X cantidad de números los cuales representan las edades de los seres humanos.

Constraints

1 ≤ D, E ≤ 10
1 ≤ X ≤ 100

Output Format

Por cada fila de la matriz imprimir la cantidad de personas que están por encima de la moda, estos números van separados por un espacio. En caso de que no exista moda imprimir para esa fila -1. Y no debes preocuparte porque no existe más de una moda.

Sample Input 0

2 5
52 21 52 100 99
20 10 50 10 56
Sample Output 0

2 3
Explanation 0

La moda en la primera fila es el número 52 y hay 2 números mayores a este.
La moda en la segunda fila es el número 10 y hay 3 números mayores a este.

Sample Input 1

4 4
42 100 33 4
88 69 46 88
52 39 28 39
34 70 34 98
Sample Output 1

-1 0 1 2
Explanation 1

En la primera fila no hay moda, se imprime -1.
La moda en la segunda fila es el número 88 y hay 0 números mayores a este.
La moda en la tercera fila es el número 39 y hay 1 número mayor a este.
La moda en la cuarta fila es el número 34 y hay 2 números mayores a este. """

D, E= map(int, input().split())
edades=[list(map(int, input().split())) for i in range(D)]
cuenta=0
mayor=0

for filas in range(D):
    for i in range(D):
        cuenta=0
        for j in range(E):
            if(edades[i] == edades[j]):
                cuenta = cuenta + 1
            if(cuenta>mayor):
                mayor=cuenta
                moda=edades[i]
    print(moda)




""" edades=[1,2,3,4,5,6,7,1,1,1,4,1,1,1,1,5,6,7]
cuenta=0
mayor=0
for i in range(len(edades)):
    cuenta=0
    for j in range(len(edades)):
        if(edades[i] == edades[j]):
            cuenta = cuenta + 1
        if(cuenta>mayor):
            mayor=cuenta
            moda=edades[i]
print(moda) """