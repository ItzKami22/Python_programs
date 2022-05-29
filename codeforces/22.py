a=int(input())
k=0
A=[int(i) for i in input().split()]
min=A[0]
max=A[0]
for i in range(1,len(A)):
    if A[i]>max:
        k+=1
        max=A[i]
    if A[i]<min:
        min=A[i]
        k+=1
print(k)
