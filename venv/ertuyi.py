a = []
n = 30
s=0
m=0
k=0
for i in range(n):
    a.append(int(input()))
for i in range(k,n):
    for i in range(k,n):
        if a[i]>=0:
            k+=1
        else:
            break
    for i in range(k, n):
        if a[i]<0:
            s+=1
            k+=1
        else:
            break
    if s>m:
        m=s
    s=0
print(m)