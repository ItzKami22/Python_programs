a=int(input())
b=0
c=0
d=0
e=0
for i in range(a):
    A = [int(i) for i in input().split()]
    b=(A[1]-A[2])*A[0]
    c=(A[1]+A[2])*A[0]
    d=A[3]-A[4]
    e=A[3]+A[4]
    if e>=b>=d:
        print('Yes')
    elif e>=c>=d:
        print('Yes')
    elif b<=d and c>=e:
        print('Yes')
    else:
        print('No')