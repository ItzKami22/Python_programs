# 1
print('#1')
M = int(input())
N = int(input())
Mat = [0] * M
for i in range(M):
    Mat[i] = [0] * N
for I in range(M):
    for i in range(N):
        Mat[I][i] = (I + 1) * 10
for row in Mat:
    print(*row)

# 2
print('#2')
M = int(input())
N = int(input())
Mat = [0] * M
for i in range(M):
    Mat[i] = [0] * N
for i in range(M):
    for J in range(N):
        Mat[i][J] = (J + 1) * 5
for row in Mat:
    print(*row)

# 3
print('#3')
M = int(input())
N = int(input())
D=float(input())
Mat = [0] * M
for i in range(M):
    Mat[i] = [int(input())] * N
a=D
for i in range(M):
    for J in range(1,N):
        Mat[i][J] = Mat[i][J]+a
        a+=D
    a=D
for row in Mat:
    print(*row)

# 4
print('#4')
M = int(input())
N = int(input())
K=int(input())
Mat = [0] * M
for i in range(M):
    Mat[i] = [int(input())] * N
print(*Mat[K])

# 5
print('#5')
M = int(input())
N = int(input())
K=int(input())
Mat = [0] * M
k=''
for i in range(M):
    Mat[i] = [int(input())] * N
    k+=str(Mat[i][K])+' '
print(k)

# 6
print('#6')
M = int(input())
N = int(input())
Mat = [0] * M
for i in range(M):
    Mat[i] = [int(input())] * N
for i in range(2,M,2):
    print(*Mat[i])

# 7
print('#7')
M,N=map(int,input().split())
Mat = [[0] * N for i in range(M)]
k = ''
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        Mat[i][j]=int(s[j])
for j in range(0, N, 2):
    for i in range(M):
        k += str(Mat[i][j])+' '
    print(k)
    k=''

# 8
print('#8')
n=int(input())
Mat=[0]*n
A=[1,1]
for i in range(n):
    Mat[i]=[0]*(i+1)
Mat[0][0]=Mat[1][0]=Mat[1][1]=1
for j in range(n-2):
    B = [1]
    for i in range(len(Mat[j+2])//2):
        B.append(A[i]+A[i+1])
    if len(Mat[j+2])%2==1:
        A=list(B)
        del B[len(B)-1]
        B.reverse()
        A.extend(B)
    else:
        del B[len(B) - 1]
        A=list(B)
        B.reverse()
        A.extend(B)
    Mat[j+2]=A
for i in range(n):
    a=""
    for j in range(n-i-1):
        a+=' '
    V=[]
    V.append(a)
    V.extend(Mat[i])
    print(*V)

# 9
print('#9')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
K=int(input("Введите K строку:"))
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
sum=0
mult=1
for i in range(N):
    sum+=mat[K-1][i]
    mult*=mat[K-1][i]
print(sum,mult)

# 10
print('#10')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
K=int(input("Введите K столбец:"))
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
sum=0
mult=1
for i in range(M):
    sum+=mat[i][K-1]
    mult*=mat[i][K-1]
print(sum,mult)

# 11
print('#11')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
    min = mat[i][0]
    for j in range(N):
        if mat[i][j]<min:
            min=mat[i][j]
    print(min)

# 12
print('#12')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
    min = mat[i][0]
    for j in range(N):
        if mat[i][j]<min:
            min=mat[i][j]
    print(min)

# 13
print('#13')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
    min = mat[i][0]
    for j in range(N):
        if mat[i][j]<min:
            min=mat[i][j]
    if i==0:
        min2=min
    if min>min2:
        min2=min
print(min2)

# 14
print('#14')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
k=0
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M):
    max = mat[i][0]
    for j in range(N):
        if mat[i][j]>=max:
            a=j
            max=mat[i][j]
    for i in range(M):
        if mat[i][a]<max:
            k+=1
    if k==0:
        print(max)
    k=0

# 15
print('#15')
M,N=map(int,input().split())
K1,K2=map(int,input().split())
mat = [[0] * N for i in range(M)]
k=0
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
mat[K1],mat[K2]=mat[K2],mat[K1]
print(' ')
for i in range(M):
    print(*mat[i])

# 16
print('#16')
M,N=map(int,input().split())
K1,K2=map(int,input().split())
mat = [[0] * N for i in range(M)]
k=0
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M):
    mat[i][K1],mat[i][K2]=mat[i][K2],mat[i][K1]
print(' ')
for i in range(M):
    print(*mat[i])

# 17
print('#17')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
    min = mat[i][0]
    max = mat[i][0]
    for j in range(N):
        if mat[i][j]<=min:
            min=mat[i][j]
            mi=j
        if mat[i][j]>=max:
            max=mat[i][j]
            ma=j
    mat[i][mi],mat[i][ma]=mat[i][ma],mat[i][mi]
for i in range(M):
    print(*mat[i])

# 18
print('#18')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for j in range(N):
    min = mat[0][j]
    max = mat[0][j]
    for i in range(M):
        if mat[i][j]<=min:
            min=mat[i][j]
            mi=i
        if mat[i][j]>=max:
            max=mat[i][j]
            ma=i
    mat[mi][j], mat[ma][j] = mat[ma][j], mat[mi][j]
print(" ")
for i in range(M):
    print(*mat[i])

# 19
print('#19')
M=int(input())
A = [[0] * M for i in range(M)]
sum=0
for i in range(M):
    s=input()
    s=s.split(' ')
    A[i][i]=int(s[i])
    sum+=A[i][i]
print(sum)

# 20
print('#20')
M=int(input())
A = [[0] * M for i in range(M)]
srar=0
for i in range(M):
    s=input()
    s=s.split(' ')
    A[i][M-i-1]=int(s[M-i-1])
    srar+=A[i][M-i-1]
print(srar/M)

# 20
print('#20')
M=int(input())
A = [[0] * M for i in range(M)]
srar=0
for i in range(M):
    s=input()
    s=s.split(' ')
    A[i][M-i-1]=int(s[M-i-1])
    srar+=A[i][M-i-1]
print(srar/M)

# 21
print('#21')
M=int(input())
A = [[0] * M for i in range(M)]
sum=0
k=0
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M):
    for j in range(i+1):
        sum+=A[j][M-1-i+j]
    print(sum)
    sum=0
for i in range(1,M):
    for j in range(M-i,0,-1):
        sum+=A[i+k][k]
        k+=1
    k=0
    print(sum)
    sum=0

# 22
print('#22')
M=int(input())
A = [[0] * M for i in range(M)]
sum=0
k=0
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M):
    min=A[0][M-i-1]
    for j in range(i+1):
        if A[j][M-1-i+j]<min:
            min=A[j][M-1-i+j]
    print(min)
for i in range(1,M):
    min = A[i][0]
    for j in range(M-i,0,-1):
        if A[i+k][k]<min:
            min=A[i+k][k]
        k+=1
    k=0
    print(min)

#Dop.zadaniya
# 23
print('#23')
k=0
l=0
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
        if mat[i][j]%2==1:
            k+=1
    if k==0:
        l=i+1
    k=0
print(l)

# 24
print('#24')
k=0
l=0
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M):
    for j in range(i+1,M):
        if mat[i]==mat[j]:
            k+=1
    if k==0:
        l+=1
    k=0
print(l)

# 25
print('#25')
mi=0
ma=0
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M):
    min=mat[0][0]
    max = mat[0][0]
    for j in range(N):
        if mat[i][j]>=max:
            max=mat[i][j]
            ma=i
        if mat[i][j]<=min:
            min=mat[i][j]
            mi=i
mat[ma],mat[mi]=mat[mi],mat[ma]
for i in range(M):
    print(*mat[i])

# 26
print('#26')
mi=0
ma=0
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M):
    min=mat[0][0]
    max = mat[0][0]
    for j in range(N):
        if mat[i][j]>=max:
            max=mat[i][j]
            ma=j
        if mat[i][j]<=min:
            min=mat[i][j]
            mi=j
for i in range(M):
    mat[i][ma],mat[i][mi]=mat[i][mi],mat[i][ma]
    print(*mat[i])

# 27
print('#27')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M):
    for j in range(i+1,M):
        if mat[j][0]<mat[i][0]:
            mat[j],mat[i]=mat[i],mat[j]
for i in range(M):
    print(*mat[i])

# 28
print('#28')
M,N=map(int,input().split())
mat = [[0] * N for i in range(M)]
for i in range(M):
    s=input()
    s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(N):
    for j in range(i+1,N):
        if mat[M-1][j]>mat[M-1][i]:
            for o in range(M):
                mat[o][j],mat[o][i]=mat[o][i],mat[o][j]
for i in range(M):
    print(*mat[i])

# 29
print('#29')
M,N=map(int,input().split())
K=int(input())
mat = [[0] * N for i in range(M+1)]
for i in range(M+1):
    if i==K:
        s=[0]*N
    else:
        s=input()
        s=s.split(' ')
    for j in range(N):
        mat[i][j]=int(s[j])
for i in range(M+1):
    print(*mat[i])

# 30
print('#30')
M=int(input())
A = [[0] * M for i in range(M)]
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M):
    for j in range(i+1,M):
        A[j][i]=0
    print(*A[i])

# 31
print('#31')
M=int(input())
A = [[0] * M for i in range(M)]
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M//2):
    for j in range(i):
        A[j][i]=0
for i in range(M//2,M):
    for j in range(M-i-1):
        A[j][i] = 0
for i in range(M):
    print(*A[i])

# 32
print('#32')
M=int(input())
A = [[0] * M for i in range(M)]
sum=0
k=0
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M):
    for j in range(i+1,M):
        A[i][j],A[j][i]=A[j][i],A[i][j]
    print(*A[i])

# 33
print('#33')
M = int(input())
A = [[0] * M for i in range(M)]
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M):
    d=''
    for j in range(M):
        d+=str(A[j][M-i-1])
        d+=' '
    print(d)


