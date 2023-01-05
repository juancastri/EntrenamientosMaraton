""" D=[]
A = []
N=int(input())
if 1 <= N <= 100:
    for i in range(N):
        ai=int(input())
        if 1<= ai <= 1000:
            D.append(ai)
    for j in range(len(D)):
        for y in range(len(D)):
            resta= D[j] - D[j+1]
            A.append(resta)
print(A) """


N=int(input())
VECTOR=[]
if 1 <= N <= 100:
    for i in range(N):
        ai=int(input())
        if 1 <= ai <= 1000:
            VECTOR.append(ai)
    contador=1
    for j in range (N-1):
        resta = N[j] - N[contador]
        resultado=abs(resta)
        contador+=1
    if resultado < N:
        print("0")
    else: 
        print("1")