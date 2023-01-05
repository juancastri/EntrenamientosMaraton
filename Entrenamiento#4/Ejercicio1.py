""" Fuiste contratado en una nueva fábrica como programador para resolver un problema muy peculiar, cada día llegaran a tus manos una lista de N ítems, los cuales debes organizar en orden ascendente, pero ten cuidado, cambiar dos ítems de posición es sumamente costoso ya que estos ítems solo pueden ser cambiados de posición por un robot. Tu tarea es decir ¿cuál es la cantidad mínima de intercambios que se deben realizar hasta ordenar el vector de forma ascendente?.

Input Format

La primera línea contiene N, el número de elementos en el arreglo. La segunda línea está compuesta por N enteros separados por espacios (ai).

Constraints

1 ≤ N ≤ 1000
1 ≤ ai ≤ 1024

Output Format

Se debe iimprimir en una línea, la cantidad mínima de intercambios hasta ordenar el vector de forma ascendente.

Sample Input 0

5
2 3 4 1 5
Sample Output 0

3
Explanation 0

Los movimientos para ordenar el arreglo [2 3 4 1 5], son:
Intercambia el #1 con el #2 [1 3 4 2 5]
Intercambia el #2 con el #3 [1 2 4 3 5]
Intercambia el #3 con el #4, quedando ordenando el vector [1 2 3 4 5]

Sample Input 1

7
1 3 5 2 4 6 7
Sample Output 1

3
Explanation 1

Los movimientos para ordenar el arreglo [1 3 5 2 4 6 7], son:
Intercambia el #2 con el #3 [1 2 5 3 4 6 7]
Intercambia el #3 con el #5 [1 2 3 5 4 6 7]
Intercambia el #4 con el #5, quedando ordenando el vector [1 2 3 4 5 6 7] """

N = int(input())
matriz=list(map(int, input().split()))
contador=0
for i in range(len(matriz)):
    for j in range(i+1,len(matriz)):
        if(matriz[j]<matriz[i]):
            temporal=matriz[j]
            matriz[j]=matriz[i]
            matriz[temporal]
            contador+=1
print(contador)



