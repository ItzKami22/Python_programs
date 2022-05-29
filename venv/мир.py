amax=10000
s=0
d_min=amax+1
N=int(input())
for i in range(N):
    a,b=map(int, input().split())
    if a>b:
        max=a
        min=b
    else:
        max=b
        min=a
    s=s+max
    if ((max-min)%5>0) and (max-min<d_min):
        d_min=max-min
if s%5==0:
    if d_min>amax:
        s=0
    else:
        s=s-d_min
print(s)