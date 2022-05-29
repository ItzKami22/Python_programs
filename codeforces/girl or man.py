a=input()
m=0
b=0
for i in a:
    for t in a:
        if i==t:
            m+=1
    if m>=2:
        a=a[:b]+a[b+1:]
        b-=1
    m=0
    b+=1
if len(a)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
