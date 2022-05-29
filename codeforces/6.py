a=int(input())
x=0
for i in range(a):
    n=input()
    for i in n:
        if i=="+":
            x+=1
            break
        elif i=="-":
            x-=1
            break
print(x)