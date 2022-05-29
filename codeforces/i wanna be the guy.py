n=int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C=[]
for i in range(n):
    C.append(i+1)
D=[]
for i in range(1,len(A)):
    if A[i] not in D:
        D.append(A[i])
for i in range(1,len(B)):
    if B[i] not in D:
        D.append(B[i])
D=sorted(D)
if C==D:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")