q=0
w=0
k=0
for i in range(5):
    A = [int(i) for i in input().split()]
    for b in range(len(A)):
        if A[b]==1:
            q=b
            w=i
while q!=2:
    if q<2:
        q+=1
        k+=1
    else:
        q-=1
        k+=1
while w!=2:
    if w<2:
        w+=1
        k+=1
    else:
        w-=1
        k+=1
print(k)