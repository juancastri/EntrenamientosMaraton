""" The slugs racing is a sport that has grown in recent years, causing several people dedicate their lives trying to capture fast slugs, and trains them to make millions in races around the world. But the task of capturing fast slugs is not an easy task, since almost all the slugs are very slow. Each slug is classified at a level depending on their speed:


Level 1: If speed is less than 10 cm/h.
Level 2: If speed is greater than or equal to 10 cm/h and lower than 20 cm/h.
Level 3: If speed is greater than or equal to 20 cm/h.


Your task is to identify which level of speed faster slug of a group of slugs.

Input
The entry consists consists multiple test cases, and each consists of two lines: The first line contains an integer L (1 ≤ L ≤ 500) representing the number of slugs of the group, and the second line contains L integers Vi (1 ≤ Vi ≤ 50) representing the speeds of each slug.
The input ends with end of file (EOF).

Output
For each test case, output a single line with the level of speed faster slug of a group of slugs. """

N=int(input())
while(N!=0):
    vector=[]
    velocidad=vector[0]
    pos=0
    cont=0
    L=int(input())
    for i in range(L):
        vi=int(input())
        vector.append(vi)
    for j in vector:
        if(j>velocidad):
            velocidad=j
            pos=cont
        cont+=1
    if(velocidad<10):
        print("slug numero %d con nivel 1" %pos)
    elif((velocidad>=10) and (velocidad<20)):
        print("slug numero %d con nivel 2" %pos)
    elif(velocidad>=20):
        print("slug numero %d con nivel 2" %pos)
    
    

