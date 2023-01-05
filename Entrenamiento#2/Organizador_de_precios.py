#Ejercicio de practica
""" Ordenar un vector de manera ascendente si es "A" o descendente si es "D" y imprimir el la cantidad de numeros
que no se movieron de su poscicion original. """

T=int(input()) #-->casos de prueba
for veces in range(T):
    X=int(input()) #-->tamaño del array
    VECTOR_ORINIGAL=list(map(int, input().split())) #-->cada uno de los elementos del array
    ORDEN=input() #--> entrada para decir si es ascendente o descendente
    VECTOR_COPIA=[]
    for i in range(X):
        VECTOR_COPIA.append(VECTOR_ORINIGAL[i])
    if(ORDEN =="A"):
        VECTOR_COPIA.sort()
    else:
        VECTOR_COPIA.sort(reverse=True)
    contador=0
    for i in range(X):
        if(VECTOR_COPIA[i]==VECTOR_ORINIGAL[i]):
            contador=contador+1
    print(contador)
