a,b=map(int,input().split())
n=0
A=[int(i) for i in input().split()]
for i in A:
    if i>=A[b-1] and i!=0:
        n+=1
print(n)