a=int(input())
k=0
v=0
for i in range(a):
    b=input()
    for n in b:
        if n!=" ":
            if int(n)==1:
                v+=1
    if v>=2:
        k+=1
    v=0
print(k)
