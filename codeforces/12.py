a=int(input())
v=0
m=0
n=0
for i in range(a):
    a, b, c = map(int, input().split())
    v+=a
    m+=b
    n+=c
if v==0 and m==0 and n==0:
    print("YES")
else:
    print("NO")