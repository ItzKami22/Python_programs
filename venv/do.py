a=[]
n=4
for i in range(n):
    a.append(int(input()))
m=0
if a[0]<a[1]:
    m+=1
if a[n-1]<a[n-2]:
    m+=1
for i in range(1,n-1):
    if a[i-1]>a[i] and a[i]<a[i+1]:
        m+=1
print(a)
