a=[]
n=6
s=0
for i in range(n):
    a.append(int(input()))
max=a[0]+a[1]+a[2]
for i in range(a):
    if a[i]+a[i+1]+a[i+2]>max:
        max=a[i]+a[i+1]+a[i+2]
        s=i
print(f'A[{s}]={a[s]}')
print(f'A[{s+1}]={a[s+1]}')
print(f'A[{s+2}]={a[s+2]}')