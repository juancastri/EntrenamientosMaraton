#THE CHILDREN OF OG THE CAVEMAN

""" Og is a caveman with many children, and he wants to count them all. Og counts his sons with his left hand
and his daughters with his right hand. However, Og is very silly, and can't add the two hands, 
so he asked you to write him a program that will do the calculation for him.image

Input Format

Each line contains two integers L and R, separated by a single space, indicating
respectively the number of sons and daughters. The end of the entry is indicated
by a line containing only two zeros, separated by a single space.

Constraints

0 ≤ L, R ≤ 5

Output Format

For each case, print a line containing an integer indicating the total number of children that Og has. """

#Primer intento
""" values=[]
L,R= 1,1 #ERROR: Estaba quemando los valores en esta linea
while L!=0 and R!=0:
    L,R=map(int,input().split())
    if (L>=0 and L<=5) and (R>=0 and R<=6):
        sum=L+R
        values.append(sum)
for i in range(len(values)-1):
    print(values[i]) """

#Segundo intento

IZQ,DER=map(int,input().split())
while(IZQ + DER != 0):
    print(IZQ + DER)
    IZQ,DER=map(int,input().split())

