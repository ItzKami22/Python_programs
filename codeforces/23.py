a=int(input())
A=[int(i) for i in input().split()]
max=0
m=0
k=0
l=0
B=[0]*100001
for i in A:
    B[i]+=1
while B!=[0]*100001:
    for n in range(len(B)):
        if B[n]*n>max:
            max=B[n]*n
            m=n
            l=1
    k+=max
    if l==1:
        B[m]=0
        B[m-1]=0
        if m!=100000:
            B[m+1]=0
    max=0
    l=0
print(k)