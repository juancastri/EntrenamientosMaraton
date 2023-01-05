""" Escriba un programa que lea un número e imprima el número de Fibonacci correspondiente al número leído.
 Recuerde que los primeros elementos de la sucesión de Fibonacci son 0 y 1,
  y cada término siguiente es la suma de los dos anteriores a él.
   Todos los números de Fibonacci calculados en este programa deben entrar en un número sin signo de 64 bits.

Entrada
La primera línea de la entrada contiene un único entero T,
 indicando el número de casos de prueba. Cada caso contiene un único entero N (0 ≤ N ≤ 60), 
 correspondiente al N-ésimo término de la sucesión de Fibonacci.

Salida
Para cada caso de prueba, imprima el mensaje "Fib(N) = X",
 donde X es el N-ésimo término de la sucesión de Fibonacci. """


#Idea inicial (funciona pero el juez no lo acepta)
Y = []
X = []
a, b = 0,1
C= 60
T = int(input())
while a < C:
    Y.append(a)
    a, b = b, a+b
for i in range(T):
    N = int(input())
    X.append(Y[N])
for j in range(T):
    print('fib({0}) = {1}'.format(N,X[j]))


#Correcion 
X = [0,1]
a, b = 0, 1
for i in range(60):
    c= a+b 
    X.append(c)
    a=b
    b=c
T = int(input())
for i in range(T):
    N = int(input())
    print('Fib(%d) = %d' %(N, X[N]))
    