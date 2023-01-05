""" Write a program that reads a number N. This N is the size of a array X[N]. 
Next, read each of the numbers of X, find the smallest element of this array and its position within the array,
 printing this information.

Input
The first line of input contains one integer N (1 < N <1000),
 indicating the number of elements that should be read to an array X[N] of integer numbers.
  The second row contains each of the N values, separated by a space.
   Remember that no input will have repeated numbers.

Output
The first line displays the message “Menor valor:”
 followed by a space and the lowest number read in the input.
  The second line displays the message “Posicao:”
   followed by a space and the array position in which the lowest number is,
    remembering that the array starts at the zero position. """

#Opcion 1
""" N=int(input())
vector=[]
lista=list(map(int, input().split()))
for i in range(N):
   vector.insert(i,lista[i])
menor= vector[0]
pos=0
for i in range(1,N):
   if(vector[i]<menor):
      menor=vector[i]
      pos=i
print("menor valor: " + str(menor))
print("posicao " +str(pos)) """

#Opcion 2: mas optimo 
""" n = int(input())
lista = list(map(int, input().split()))
p = 0
m = lista[0]
count = 0
for i in lista:
    if (i < m):
        m = i
        p = count
    count += 1
print("Menor valor: %d" % m)
print("Posicao: %d" % p) """