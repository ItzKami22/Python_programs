a=int(input())
A=[int(i) for i in input().split()]
B=[]
p=0
h=a//2
M=[]
j=2
c=1
while a>1:
    a=a//2
    p+=1
for i in range(p):
    for z in range(1,h+1):
        for x in range(j,0,-1):
            M.append(A[z*j-x])
        B=sorted(M)
        if M==B:
            c=len(M)
        M=[]
    h=h//2
    j=j*2
print(c)
