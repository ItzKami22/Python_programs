a=int(input())
A=[int(i) for i in input().split()]
B=sorted(A)
p=0
n=0
k=2
while a>1:
    a=a//2
    p+=1
def sort(x):
    d=[]
    for i in range(0,len(x)//2):
        d.append(x[i])
    if d==sorted(d):
        return len(d)
def sort2(x):
    y=[]
    for i in range(len(x) // 2,len(x)):
        y.append(x[i])
    if y==sorted(y):
        return len(y)
if B==A:
    print(len(A))
else:
    for i in range(p):
        if sort(A)==None and sort2(A)!=None:
            n=sort2(A)
            break
        elif sort(A)!=None and sort2(A)==None:
            n=sort(A)
            break
        elif sort(A)!=None and sort2(A)!=None:
            n=sort(A)
            break
        elif sort(A)==None and sort2(A)==None:
            for i in range(k):
