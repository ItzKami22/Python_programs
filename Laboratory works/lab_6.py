#1
print('#1')
def DigitCountSum(K, C, S):
    while K>0:
        S += K % 10
        K //= 10
        C += 1
    return (C, S)

for i in range(5):
    K=int(input())
    C=0
    S=0
    print(DigitCountSum(K,C,S))

#2
print('#2')
def AddRightDigit(D, K):
    K*=10
    K+=D
    return K
K=int(input())
D1=int(input())
D2=int(input())
print(AddRightDigit(D1,K))
print(AddRightDigit(D2,AddRightDigit(D1,K)))

#3
print('#3')
def AddLeftDigit(D, K):
    K2=K
    k=0
    while K2>0:
        k+=1
        K2//=10
    K+=(10**k)*D
    return K

K = int(input())
D1 = int(input())
D2 = int(input())
print(AddLeftDigit(D1, K))
print(AddLeftDigit(D2, AddLeftDigit(D1, K)))

#4
print('#4')
def Swap(X, Y):
    f=X
    X=Y
    Y=f
    return(X,Y)
A = int(input())
B = int(input())
C = int(input())
D = int(input())
Swap(A, B)
Swap(C, D)
Swap(B, C)
A,B=Swap(A,B)
C,D=Swap(C,D)
B,C=Swap(B,C)
print(A,B,C,D)

#5
print('#5')
def Minmax(X, Y):
    f=X
    X=min(X,Y)
    Y=max(f,Y)
    return(X,Y)
A = float(input())
B = float(input())
C = float(input())
D = float(input())
A,B=Minmax(A, B)
C,D=Minmax(C, D)
B,D=Minmax(B, D)
A,C=Minmax(A, C)
print(A,D)

#6
print('#6')
def Min(a,b):
    if a==0:
        return 0
    b=min(b,a)
    return b
a = int(input())
b=a
while True:
    a = int(input())
    if Min(a,b)==0:
        break
    b=Min(a,b)
print(b)

#7
print('#7')
def Minmax():
    a = int(input())
    c = a
    b=a
    while True:
        a=int(input())
        c = max(c, a)
        b=min(b,a)
        if a==0:
            break
    return c, b
print(*Minmax())

#8
print('#8')
def SortDec3(A,B,C):
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A
    return C, B, A

A1,B1,C1=map(int,input().split())
A2,B2,C2=map(int,input().split())
print(*SortDec3(A1,B1,C1))
print(*SortDec3(A2,B2,C2))

#9
print('#9')
def ShiftRight3(A,B,C):
    A,B,C=C,A,B
    return A,B,C
A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
print(*ShiftRight3(A1,B1,C1))
print(*ShiftRight3(A2,B2,C2))

#10
print('#10')
def ShiftLeft3(A,B,C):
    A,B,C=B,C,A
    return A,B,C
A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
print(*ShiftLeft3(A1,B1,C1))
print(*ShiftLeft3(A2,B2,C2))

#11
import math
print('#11')
b=0
def IsSquare(K):
    if math.sqrt(K)%1==0:
        return True
    else:
        return False
for i in range(10):
    a=int(input())
    if IsSquare(a):
        b+=1
print(b)

#12
import math
print('#12')
def DigitCount(K):
    k=0
    while K>0:
        k+=1
        K//=10
for i in range(5):
    a=int(input("Введите целое положительное число"))

#13
print('#13')
def DigitN(K, N):
    if len(str(K))<K//(10**N)%10:
        return -1
    else:
        return K//(10**N)%10
for i in range(5):
    a=int(input())
    for j in range(len(str(a))):
        print(DigitN(a,j))

#14
print('#14')
def Fact(N):
    f=1
    while N>0:
        f*=N
        N-=1
    return f
for i in range(5):
    N=int(input())
    print(Fact(N))

#15
print('#15')
def Fact2(N):
    f=1
    for i in range(N%2,N+1,2):
        if i!=0:
            f*=i
    return f
for i in range(5):
    N=int(input())
    print(Fact(N))

#16
print('#16')
def NOD2(A,B):
    while A != 0 and B != 0:
        if A > B:
            A = A % B
        else:
            B = B % A
    return A+B
A,B,C,D=map(int,input().split())
print(NOD2(A,B))
print(NOD2(A,C))
print(NOD2(A,D))

#17
print('#17')
def IncTime(H,M,S,T):
    S+=T
    M+=S//60
    S%=60
    H+=M//60
    M%=60
    return H,M,S
H, M, S = map(int, input().split())
T=int(input())
print(IncTime(H,M,S,T))

#18
print('#18')
def Calc(A, B, Op):
    if Op==1:
        return A-B
    elif Op==2:
        return A*B
    elif Op==3:
        return A/B
    else:
        return A+B
A,B=map(int, input().split())
Op=int(input())
print(Calc(A,B,Op))

#Доп. задания
#19
print('#19')
def kef(n):
    a=int(input())
    max=a
    min=a
    for i in range(n-1):
        a=int(input())
        if a>max:
            max=a
        if a<min:
            min=a
    return min, max
n=int(input())
print(*kef(n))

#20
print('#20')
n=int(input())
k=int(input())
def wfl(n,k):
    return (n//(10**(k-1)))%10
print(wfl(n,k))

#21
print('#21')
n=input()
def desf(n):
    s=0
    for i in range(len(n)):
       s+=int(n[len(n)-1-i])*2**i
    return s
def dvf(s):
    dv=''
    while s>0:
        dv+=str(s%2)
        s//=2
    return dv [::-1]
s=desf(n)
print(s)
print(dvf(s))

#22
print('#22')
n=input()
def des(n):
    sh=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    dv=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    s=''
    for i in range(len(n)):
        for j in range(len(sh)):
            if n[i]==sh[j]:
                s+=dv[j]
    de = 0
    for i in range(len(s)):
        de += int(s[len(s) - 1 - i]) * 2 ** i
    return de
def she(s):
    dvo = ''
    while s > 0:
        dvo += str(s % 2)
        s //= 2
    dvo=dvo[::-1]
    sh = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dv = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
          '1101', '1110', '1111']
    she=''
    l=''
    for i in range(len(dvo)):
        if i%4!=0 or i==0:
            l+=dvo[i]
        else:
            l=''
            l += dvo[i]
        if len(l)==4:
            for j in range(len(dv)):
                if l==dv[j]:
                    she+=sh[j]
    return she
s=des(n)
print(s)
print(she(s))

#23
print('#23')
n=input()
def dvf(n):
    sh=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    dv=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    s=''
    for i in range(len(n)):
        for j in range(len(sh)):
            if n[i]==sh[j]:
                s+=dv[j]
    return s
def she(s):
    sh = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dv = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
          '1101', '1110', '1111']
    she=''
    l=''
    for i in range(len(s)):
        if i%4!=0 or i==0:
            l+=s[i]
        else:
            l=''
            l += s[i]
        if len(l)==4:
            for j in range(len(dv)):
                if l==dv[j]:
                    she+=sh[j]
    return she
s=dvf(n)
print(she(s))

#24
def Robot(k,C,N,k1,k2,k3,k4,kl):
    if N==-1:
        if C=="С":
            C="В"
        elif C=="В":
            C ="Ю"
        elif C=="Ю":
            C ="З"
        else:
            C ="С"
    elif N==1:
        if C=="С":
            C ="З"
        elif C=="В":
            C ="С"
        elif C=="Ю":
            C ="В"
        else:
            C ="Ю"
    else:
        if C=="С":
            k1+=1
            kl+=1
        if C == "В":
            k2 += 1
            kl += 1
        if C == "Ю":
            k3 += 1
            kl += 1
        if C == "З":
            k4 += 1
            kl += 1
    if k1==2*k+1//2 or k2==2*k+1//2 or k3==2*k+1//2 or k4==2*k+1//2:
        return C, kl
    return C, kl
print('#24')
k=int(input())
na=''
k1=0
k2=0
k3=0
k4=0
kl=0
C=input("Введите направление:")
for i in range(k):
    N=int(input("Введите номер действия: 0-продолжить движение,1-поворот налево, -1-поворот направо:"))
    C,kl=Robot(k,C,N,k1,k2,k3,k4,kl)
print(C,kl)
