#INTERCAMBIO DE MATRICES 
""" Tu tarea es intercambiar la informacion en las columnas de la matriz.
intercambiar el primero con el ultimo, el segundo con el penultimo y asi sucesivamente con los demas. """

t=int(input())
for veces in range(1, t+1):
    r,c = map(int, input().split())
    mat=[]
    for i in range(r):
        mat.append(list(map(int, input().split())))
    for i in range(r):
        for j in range(c//2):
            aux=mat[i][j]
            mat[i][j]=mat[i][c-j-1]
            mat[i][c-j-1]=aux
    for i in range(r):
        for j in range(c):
            print(mat[i][j],'',end=" ")
        print('') 
