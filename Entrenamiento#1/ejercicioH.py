""" En este problema debes leer 15 números y guardarlos en dos arreglos diferentes: 
par si el número es par o impar si el número es impar.
Pero el tamaño de cada arreglo es solo de 5 posiciones.
Por esto, cada vez que llenes uno de los dos arreglos,
deberás imprimir el arreglo entero para poder usarlo nuevamente para los siguientes números a leer.
Al final,todos los números restantes de cada uno de estos arreglos debe ser impreso comenzando con el arreglo par.
Cada arreglo puede ser rellenado cuantas veces sea necesario.

Entrada
La entrada consiste de 15 números enteros.

Salida
Imprima la salida como en el siguiente ejemplo: """
par = []
impar = []
for i in range(15):
    value=int(input())
    if (len(par) <= 5) and (len(impar) <= 5):
        if value % 2 == 0:
            par.append(value)
        else:
            impar.append(value)
    if (len(par) == 5):
        for i in range(5):
            print('par[{0}] = {1}'.format(i,par[i]))
        par.clear()
    elif (len(impar) == 5):
        for i in range(5):
            print('impar[{0}] = {1}'.format(i,impar[i]))
        impar.clear()
for i in range(2):
            print('impar[{0}] = {1}'.format(i,impar[i]))
for i in range(3):
            print('par[{0}] = {1}'.format(i,par[i]))


""" par = []
impar = []
for i in range(15):
    valor = int(input())
    if(valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)
    
    if(len(par)==5):
        ix = 0
        for v in par:
            print("par[%d] = %d" %(ix,v))
            ix += 1
        par = []
    if(len(impar)==5):
        ix = 0
        for v in impar:
            print("impar[%d] = %d" %(ix,v))
            ix += 1
        impar = []
if(len(impar)> 0):
    ix = 0
    for v in impar:
        print("impar[%d] = %d" %(ix,v))
        ix += 1

if(len(par)>0):
    ix = 0
    for v in par:
        print("par[%d] = %d" %(ix,v))
        ix += 1 """ 
