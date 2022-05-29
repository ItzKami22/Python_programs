import random
from random import randint

#1
print('#1')
n = int(input("Введите число N:"))
i = 1
s = [i]
while i != n:
    i += 2
    s.append(i)
print('Ответ:', s)
print()

#2
print('#2')
n = int(input("Введите число N:"))
a = int(input("Введите число A:"))
d = int(input("Введите число D:"))
s = [a]
for i in range(1, n):
    k = a + d * i
    s.append(k)
print('Ответ:', s)
print()

#3
print("#3")
n = int(input("Введите число N:"))
a = int(input("Введите число A:"))
b = int(input("Введите число B:"))
s = [a, b]
c = 0
for i in range(2, n):
    c = sum(s)
    s.append(c)
print('Ответ:', s)
print()

#4
print("#4")
n = int(input("Введите число N:"))
k = 0
s = int
s = [1]
for i in range(1, n):
    s.append(random.randint(1, 1000))
for i in range(0, n):
    if s[i] % 2 == 1:
        print(s[i])
        k += 1
print('Ответ:', "K =", k)
print()

#5
print("#5")
n = int(input("Введите число N:"))
k = 0
s = int
s = [1]
for i in range(1, n):
    s.append(random.randint(1, 123))
while n != 0:
    if s[n - 1] % 2 == 0:
        print(s[i])
        k += 1
    n -= 1
print('Ответ:', "K =", k)
print()

#6
print("#6")
a = [1]
n = int(input("Введите число N:"))
for i in range(1, n):
    a.append(random.randint(1, 1000))
print(a)
i = 1
while i <= n:
    print(a[i])
    i += 2
print()

#7
print("#7")
a = []
for i in range(0, 10):
    a.append(random.randint(1, 1000))
print('A =', a)
j = 0
while j < 9:
    if a[j] < a[9]:
        print('Ответ:', a[j])
        break
    j += 1
if j == 9:
    print(0)
print()

#8
print("#8")
n = int(input("Введите число N:"))
k = int(input("Введите число K:"))
l = int(input("Введите число L:"))
a = [1]
s = 0
for i in range(1, n):
    a.append(random.randint(1, 1000))
i = 0
print(a)
for i in range(k - 1, l):
    s = a[i] + s
print("Ответ: Сумма элементов от K до L включительно равна", s)
print()

#9
print("#9")
n = int(input("Введите число N:"))
k = int(input("Введите число K:"))
l = int(input("Введите число L:"))
a = [1]
s = 0
for i in range(1, n):
    a.append(random.randint(1, 1000))
print(a)
for i in range(0, k - 1):
    s = a[i] + s
for i in range(l, n):
    s = a[i] + s
print('Ответ:', s)
print()

#10
print("#10")
n = int(input("Введите число N:"))
a = []
i = 1
for i in range(0, n):
    a.append(random.randint(-100, 100))
print("A =", a)
i = 0
while i != n:
    if (a[i] % 2 == 1 and a[i - 1] % 2 == 0):
        i += 1
    elif (a[i] % 2 == 0 and a[i - 1] % 2 == 1):
        i += 1
    else:
        print('Ответ:', i + 1)
        break
if i == n:
    print('Ответ:', 0)
print()

#11
print("#11")
n = int(input("Введите число N:"))
a = []
for i in range(0, n):
    a.append(random.randint(-100, 100))
min = 100
print("A =", a)
i = 0
while i < n:
    if a[i] < min:
        min = a[i]
    i += 2
print("Ответ:", min)
print()

#12
print("#12")
n = int(input("Введите число N:"))
a = []
s = 0
for i in range(0, n):
    a.append(random.randint(-100, 100))
i = 1
print(a)
print("Ответ:")
while i != n:
    if a[i] > a[i - 1]:
        print(i + 1)
        s += 1
    i += 1
print("Кол-во элементов, больших чем правый сосед, равно:", s)
print()

#13
print("#13")
n = int(input("Введите число N:"))
a = []
for i in range(0, n):
    a.append(random.randint(-100, 100))
print("A =", a)
i = 1
while i != n:
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        print("Ответ:", i + 1)
        break
    i += 1

#14
print("#14")
N = int(input('Введите N:'))
A = [randint(0, 10) for i in range(N)]
B = [randint(0, 10) for i in range(N)]
print('A = ', A)
print('B = ', B)
C = [randint(0, 10) for i in range(N)]
for i in range(N):
    if A[i] > B[i]:
        C[i] = A[i]
    else:
        C[i] = B[i]
print('Ответ:')
print('C = ', C)
print()

#15
print("#15")
N = int(input('Введите N:'))
B = []
counter = 0
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
for i in range(N):
    if A[i] % 2 == 0:
        B.append(A[i])
        counter += 1
print('Ответ: Размер B =', counter)
print('B = ', B)
print()

#16
print("#16")
N = int(input('Введите N:'))
B = []
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
for i in range(0, N, 2):
    B.append(A[i])
for i in range(1, N, 2):
    B.append(A[i])
print('Ответ:')
print('B = ', B)
print()

#17
print("#17")
N = int(input('Введите N:'))
B = []
C = []
counterB = 0
counterC = 0
A = [randint(-10, 10) for i in range(N)]
print('A = ', A)
for i in range(N):
    if A[i] >= 0:
        B.append(A[i])
        counterB += 1
    else:
        C.append(A[i])
        counterC += 1
print('Ответ:')
print(' Размер B =', counterB, ', B = ', B)
print(' Размер C =', counterC, ', C = ', C)
print()

#18
print("#18")
A = []
B = []
C = []
for i in range(5):
    A.append(random.randint(1, 10))
    B.append(random.randint(1, 10))
A.sort()
B.sort()
for i in range(5):
    C.append(A[i])
    C.append(B[i])
C.sort()
print('A = ', A)
print('B = ', B)
print("Ответ:")
print('C = ', C)
print()

#19
print("#19")
N = int(input('Введите N:'))
K = int(input('Введите K:'))
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
for i in range(N):
    A[i] += K
print('Ответ:')
print('А[i+k] = ', A)
print()

#20
print("#20")
N = int(input('Введите N:'))
min = 10
minI = -1
max = 0
maxI = -1
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
for i in range(N):
    if A[i] > max:
        max = A[i]
        maxI = i
    if A[i] < min:
        min = A[i]
        minI = i
A[maxI] = min
A[minI] = max
print('Ответ:')
print('A = ', A)
print()

#21
print("#21")
N = int(input('Введите N (N — четное число):'))
i = 0
t = 0
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
for i in range(0, N - 1, 2):
    t = A[i + 1]
    A[i + 1] = A[i]
    A[i] = t
print('Ответ:')
print('A = ', A)
print()

#22
print("#22")
N = int(input('Введите N:'))
l = 0
minI = -1
r = 0
maxI = -1
max = 0
min = 10
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
for i in range(N):
    if A[i] > max:
        max = A[i]
        maxI = i
    if A[i] < min:
        min = A[i]
        minI = i
if maxI > minI:
    r = maxI
    l = minI
else:
    r = minI
    l = maxI
while (l + 1 != r):
    A[l + 1] = 0
    l += 1
print('Ответ:')
print('A = ', A)
print()

#23
print("#23")
N = int(input('Введите N:'))
k = 0
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
t = A[N - 1]
for i in range(N - 2, 0, -1):
    k = A[i]
    A[i] = t
    t = k
A[0] = t
A[N - 1] = 0
print('Ответ:')
print('A = ', A)
print()

#24
print("#24")
N = int(input('Введите N:'))
K = int(input('Введите K:'))
k = 0
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
del A[K - 1]
print('Ответ:')
print('A = ', A)
print()

#25
print("#25")
N = int(input('Введите N:'))
K = int(input('Введите K:'))
L = int(input('Введите L:'))
k = 0
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
k = L - K
for i in range(k + 1):
    del A[K - 1]
print('Ответ:', len(A), "эл.")
print('A = ', A)
print()

#26
print("#26")
N = int(input('Введите N:'))
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
B = []
for i in range(N):
    if A[i] % 2 == 0:
        B.append(A[i])
print('Ответ:', len(B), "эл.")
print('B = ', B)
print()

#27
print("#27")
N = int(input('Введите N:'))
A = [randint(0, 10) for i in range(N)]
print('A = ', A)
B = []
for i in range(N - 1):
    if A[i] != A[i + 1]:
        B.append(A[i])
if A[N - 1] != A[N - 2]:
    B.append(A[N - 1])
print('Ответ:')
print('B = ', B)
print()

#Dop.zadaniya
#28
print("#28")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
A.sort()
B=[0]*(A[-1]+1)
m=0
if A[0]<0:
    C=[0]*(-A[0]+1)
    m=1
for i in range(N):
    if A[i]>=0:
        B[A[i]]+=1
    else:
        C[-A[i]]+=1
B.sort()
if m==1:
    C.sort()
    ma=max(B[-1],C[-1])
    print(ma)
else:
    print(B[-1])

#29
print("#29")
N=int(input("Введите длину массива:"))
A = list(map(str,input("Введите элементы массива:").split(maxsplit = N)))
B=[]
C=[]
for i in range(N):
    if i<N//2:
        B.append(A[i])
    else:
        C.append(A[i])
A=C+B
print(*A)

#30
print("#30")
N=int(input("Введите длину массива:"))
A = list(map(str, input("Введите элементы массива:").split(maxsplit = N)))
K=int(input("Введите число K:"))
for i in range(K):
    A.insert(0, A[N-1])
    del A[N]
print(*A)

#31
print("#31")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
A.sort()
B=[0]*(A[-1]+1)
m=0
if A[0]<0:
    C=[0]*(-A[0]+1)
    m=1
for i in range(N):
    if A[i]>=0:
        B[A[i]]+=1
    else:
        C[-A[i]]+=1
A=[]
for i in range(len(B)):
    if B[i]>=3:
        for j in range(B[i]):
            A.append(i)
if m==1:
    for i in range(len(C)):
        if B[i]>=3:
            for j in range(B[i]):
                A.append(i)
print(len(A))
print(*A)

#32
print("#32")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
A.sort()
B=[0]*(A[-1]+1)
m=0
if A[0]<0:
    C=[0]*(-A[0]+1)
    m=1
for i in range(N):
    if A[i]>=0:
        B[A[i]]+=1
    else:
        C[-A[i]]+=1
A=[]
for i in range(len(B)):
    if B[i]>=1:
        A.append(i)
if m==1:
    for i in range(len(C)):
        if B[i]>=1:
            A.append(i)
print(*A)

#33
print("#33")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
A.sort()
B=[0]*(A[-1]+1)
m=0
if A[0]<0:
    C=[0]*(-A[0]+1)
    m=1
for i in range(N):
    if A[i]>=0:
        B[A[i]]+=1
    else:
        C[-A[i]]+=1
A=[]
for i in range(len(B)):
    if B[i]!=2 and B[i]!=0:
        for j in range(B[i]):
            A.append(i)
if m==1:
    for i in range(len(C)):
        if C[i]!=2 and C[i]!=0:
            for j in range(C[i]):
                A.append(-i)
print(len(A))
print(*A)

#34
print("#34")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
mi=0
ma=0
for i in range(N):
    if A[i]>A[ma]:
        ma=i
    if A[i]<A[mi]:
        mi=i
A.insert(mi,0)
A.insert(ma+2,0)
print(*A)

#35
print("#35")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
B=A
k=0
for i in range(1,N,2):
    B.insert(i+k,A[i+k])
    k+=1
print(*B)

#36
print("#36")
N=int(input("Введите длину массива:"))
A = list(map(int, input("Введите элементы массива:").split(maxsplit = N)))
B=[]
C=[]
k=A[0]
D=[A[0]]
b=1
for i in range(1,N):
    if A[i]==k:
        b+=1
        D.append(A[i])
        k=A[i]
        if i==N-1:
            B.append(b)
            C.append(D)
    else:
        B.append(b)
        C.append(D)
        k=A[i]
        D = [A[i]]
        b=1
        if i==N-1:
            B.append(b)
            C.append(D)
print(*B)
print()
for i in C:
    print(*i)