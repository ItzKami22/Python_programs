a=input()
a=a.lower()

for i in a:
    if i=="a" or i=="o" or i=='e' or i=='y' or i=='u' or i=='i':
        a=a.replace(i,'')
for i in range(0,len(a)*2,2):
    a=a[:i]+'.'+a[i:]
print(a)