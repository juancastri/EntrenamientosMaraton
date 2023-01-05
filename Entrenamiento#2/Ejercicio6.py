#POOR, PERFECT AND ABUNDANT 1
"""  
Decimos que un número es ABUNDANTE, cuando la suma de sus divisores propios es mayor que él.
Decimos que un número es POBRE, cuando la suma de sus divisores propios es menor que él.
Decimos que un número es PERFECTO, cuando la suma de sus divisores propios es igual a él.

Formato de entrada

La línea de entrada es un número entero N.

Restricciones

2 ≤ norte ≤ 10^10

Formato de salida

Imprima si el número es POBRE, PERFECTO o ABUNDANTE

Entrada de muestra 0

10
Salida de muestra 0

POBRE
Explicación 0

Para el Ejemplo#1: el número 10 es POBRE porque sus divisores, 1, 2 y 5 sumaron 8 que es menor que 10.

Entrada de muestra 1

12
Salida de muestra 1

ABUNDANTE
Explicación 1

Para el Ejemplo#2: el número 12 es ABUNDANTE porque sus divisores, 1, 2, 3, 4 y 6 tienen 16 que es mayor que 12.

Entrada de muestra 2

6
Salida de muestra 2

PERFECTO
Explicación 2

Para el Ejemplo #3, el Número 6 es PERFECTO porque sus divisores, 1, 2 y 3 suman 6 que es igual a 6."""

N=int(input())
array=[]
for divisor in range(1,N):
    if(N % divisor) == 0:
        array.append(divisor)
suma=sum(array)
if (suma > N):
        print("ABUNDANT")
elif (suma < N):
        print("POOR")
else:
        print("PERFECT") 