N=int(input())
b=0
a=[]
for i in range(N):
    a.append(int(input()))
for i in range(N-4):
    for q in range(i+4,N):
        if a[i]*a[q]%29==0:
            b+=1
print(b)
