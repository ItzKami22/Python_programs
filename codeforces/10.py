a=input()
a=a.split("WUB")
a=' '.join(a)
if a[0]==' ':
    a=a[1:]
if a.find('  '):
    a=a.replace('  ',' ')
print(a)

