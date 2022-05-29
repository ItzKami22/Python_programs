a=int(input())
A=[]
for i in range(a):
    d=input()
    if len(d)>=11:
        d=d[0]+str(len(d)-2)+d[-1]
    A.append(d)
for i in A:
    print(i)