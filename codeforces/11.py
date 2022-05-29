a=int(input())
b=0
c=0
d=0
A=[int(i) for i in input().split()]
for i in A:
    b+=i
A=reversed(sorted(A))
for i in A:
    if c<=b//2:
        c+=i
        d+=1
print(d)