a=input()
b=input()
a=a.lower()
b=b.lower()
for i in range(len(a)):
    if ord(a[i])>ord(b[i]):
        print(1)
        break
    elif ord(a[i])<ord(b[i]):
        print(-1)
        break
    if i==len(a)-1:
        print(0)