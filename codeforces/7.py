a,b,c=map(int,input().split())
if a%c==0 and b%c==0:
    print((a//c)*(b//c))
elif a%c!=0 and b%c!=0:
    print((a//c+1)*(b//c+1))
elif a%c!=0 and b%c==0:
    print((a//c+1)*(b//c))
else:
    print((a//c)*(b//c+1))
