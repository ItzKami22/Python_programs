import math
import random
q=int(input())
def fact(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    print("Факториал:", fact)
def dvo(x):
    dv=''
    while x>0:
        dv+=str(x%2)
        x//=2
    print("В 2-чной:",dv[::-1])
def vos(x):
    vo=''
    while x>0:
        vo+=str(x%8)
        x//=8
    print("В 8-чной:",vo[::-1])
def she(x):
    sh=''
    shes=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    while x>0:
        sh+=str(shes[x%16])
        x//=16
    print("В 16-чной:",sh[::-1])
def cube(x):
    print("В кубе:",x**3)
def prikol(x):
    ran=""
    for i in range(int(math.sqrt(x))):
        ran+=chr(random.randint(0,x))
    print("Рандомная хрень(или нет...):",ran)
fact(q)
dvo(q)
vos(q)
she(q)
cube(q)
print("Умноженное на пи:",math.pi*q)
print("Знак свыше:",chr(q))
prikol(q)