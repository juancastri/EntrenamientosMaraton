#Array Replacement I#
""" Read an array X[10]. After, replace every null or negative number of X ​by 1.
 Print all numbers stored in the array X. 
 Input:
The input contains 10 integer numbers. These numbers ​​can be positive or negative.
Output:
For each position of the array, print "X [i] = x",
 where i is the position of the array and x is the number stored in that position."""


""" Intento 1 realizado por mi, --Buena logica, pude resolver el problema pero no encontre la manera de concatenar
de manera que el juez lo leyera  """
""" x = []
c = 0
for i in range(1,11,1):
    i = int(input())
    x.append(i)
for j in range(len(x)):
    if x[j] <= 0:
        x[j] = 1
for n in x:
    print(f"x[{c}] = {n}") <--- #este tipo de concatenacion no la acepta el juez  
    c += 1   """


#Buscado en internet como apoyo
""" X = []
for i in range(10):
    value = int(input())
    if value <= 0:
        value = 1
        X.insert(i,value)
    else:
        X.insert(i,value)

for i in range(10):
    print('X[{0}] = {1}'.format(i,X[i]))  """

#modificado a mi manera con base en el ejemplo de interne pero con mi logica. 
X = []
for i in range(10):
    value = int(input())
    X.append(value)
for j in range(10):
    if X[j] <= 0:
        X[j] = 1
for i in range(10):
    print('X[{0}] = {1}'.format(i, X[i])) #<--- este tipo de concatenacion si la acepta el juez