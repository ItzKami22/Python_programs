import os.path
#1
print('#1')
S=input("Введите название для файла:")
f=open(S,"w")
f.close()
print(os.path.exists(S))

#2
print('#2')
S=input("Введите название для файла:")
N=int(input("Введите целое число большее 1:"))
f=open(S,"w")
f.write("2")
for i in range(2,N+1):
    f.write(", "+str(i*2))
f.close()

#3
print('#3')
A, B, C, D=map(str,input("Введите 4 названия файлов:").split())
k=0
if os.path.exists(A)==True:
    k+=1
if os.path.exists(B)==True:
    k+=1
if os.path.exists(C)==True:
    k+=1
if os.path.exists(D)==True:
    k+=1
print(k)

#4
print('#4')
S=input("Введите название для файла:")
if os.path.exists(S)==False:
    print(-1)
else:
    f=open(S, "r")
q=f.read()
q=q.split()
print(len(q))
f.close()

#5
print('#5')
f=open(input("Введите название файла:"),"r")
d=f.read()
d=d.split()
print(d[0],d[1],d[-2],d[-1])
f.close()

#6
print('#6')
f=open(input("Введите название файла:"),"r")
d=f.read()
d=d.split()
d.reverse()
d=' '.join(d)
f.close()
fi=open(input("Введите название второго файла:"),"w")
fi.write(d)
fi.close()

#7
print('#7')
f=open(input("Введите название файла:"),"r")
d=f.read()
d=d.split()
f1=open(input("Введите название 1-го файла:"),"w")
f2=open(input("Введите название 2-го файла:"),"w")
for i in range(len(d)):
    if i%2==0:
        f1.write(d[i]+' ')
    else:
        f2.write(d[i]+' ')
f.close()
f1.close()
f2.close()

#8
print('#8')
f=open(input("Введите название файла:"),"r+")
d=f.read()
d=d.split()
for i in range(len(d)):
    d[i]=str(int(d[i])**2)
d=' '.join(d)
f.seek(0)
f.write(d)
f.close()

#9
print('#9')
f=open(input("Введите название файла:"),"r+")
d=f.read()
d=list(d.split())
min=d[0]
max=d[0]
for i in range(len(d)):
    if int(d[i])<= int(min):
        min=d[i]
    if int(d[i])>=int(max):
        max=d[i]
h=d.index(min)
g=d.index(max)
d[h],d[g]=d[g],d[h]
d=' '.join(d)
f.seek(0)
f.write(d)
f.close()


#10
print('#10')
S=input("Введите название файла:")
f=open(S,"r")
x=[]
d=f.read()
d=d.split()
for i in range(len(d)//2):
    x.append(d[i])
x=' '.join(x)
f.close()
f=open(S,"w")
f.write(x)
f.close()


#11
print('#11')
S=input("Введите название файла:")
f=open(S,"r")
x=[]
d=f.read()
d=d.split()
for i in range(0,len(d),2):
    x.append(d[i])
x=' '.join(x)
f.close()
f=open(S,"w")
f.write(x)
f.close()

#12
print('#12')
S=input("Введите название файла:")
f=open(S,"r")
x=[]
d=f.read()
d=d.split()
for i in range(len(d)):
    if int(d[i])>=0:
        x.append(d[i])
x=' '.join(x)
f.close()
f=open(S,"w")
f.write(x)
f.close()

#13
print('#13')
S=input("Введите название файла:")
f=open(S,"r+")
x=[]
d=f.read()
f.write(d)
f.close()

#14
print('#14')
S=input("Введите название файла:")
f=open(S,"r")
d=f.read()
d=d.split()
x=d
f.close()
f=open(S,"w")
for i in range(len(d)):
    f.write(d[i])
    f.write(" ")
    if i%2==0:
        f.write(d[i])
        f.write(" ")
f.close()

#15
print('#15')
S=input("Введите название файла:")
f=open(S,"r")
d=f.read()
d=d.split()
x=d
f.close()
f=open(S,"w")
for i in range(len(d)):
    if i%2==1:
        f.write("0 0 ")
    else:
        f.write(d[i]+" ")
f.close()

#16
print('#16')
S1=input("Введите название 1 файла:")
f1=open(S1,"rb")
S2=input("Введите название 2 файла:")
f2=open(S2,"rb")
a=f1.read()
b=f2.read()
f1,f2.close()
f1=open(S1,"wb")
f2=open(S2,"wb")
f1.write(b)
f2.write(a)
f1,f2.close()

#17
print('#17')
S1=input("Введите название файла:")
f1=open(S1,"rb")
S2=input("Введите название копии файла:")
f2=open(S2,"wb")
a=f1.read()
f2.write(a)
f1,f2.close()

#18
print('#18')
t1=input("Введите тип файлов:")
S1=input("Введите название 1 файла:")
f1=open(S1,"r"+t1)
S2=input("Введите название 2 файла:")
f2=open(S2,"r"+t1)
S3=input("Введите название 3 файла:")
f3=open(S3,"r"+t1)
a=f1.read()
b=f2.read()
c=f3.read()
f1,f2,f3.close()
if len(c)<=len(a)>=len(b):
    f1 = open(S1, "w" + t1)
    max=a
    q=f1
elif len(b)<=len(c)>=len(a):
    f3 = open(S3, "w" + t1)
    max=c
    q=f3
else:
    f2 = open(S2, "w" + t1)
    max=b
    q=f2
if len(c)>=len(a)<=len(b):
    min=a
    f1 = open(S1, "w" + t1)
    f1.write(max)
elif len(b)>=len(c)<=len(a):
    min=c
    f3 = open(S3, "w" + t1)
    f3.write(max)
else:
    min=b
    f2 = open(S2, "w" + t1)
    f2.write(max)
q.write(min)
f1,f2,f3.close()

#19
print('#19')
t1=input("Введите тип файлов:")
S1=input("Введите название 1 файла:")
f1=open(S1,"r"+t1+"+")
S2=input("Введите название 2 файла:")
f2=open(S2,"r"+t1+"+")
a=f1.read()
b=f2.read()
f2.write(a)
f1.write(b)
f1,f2.close()

#Dop. zadaniya
#20
print('#20')
S1=input("Введите название файла:")
f1=open(S1,"r")
S2=input("Введите название 1 файла:")
f2=open(S2,"w")
S3=input("Введите название 2 файла:")
f3=open(S3,"w")
a=f1.read()
a=a.split()
a.reverse()
for i in range(len(a)):
    if int(a[i])<0:
        f3.write(a[i]+' ')
    else:
        f2.write(a[i]+' ')
f1,f2,f3.close()

#21
print('#21')
S1=input("Введите название 1 файла:")
f1=open(S1,"r")
S2=input("Введите название 2 файла:")
f2=open(S2,"r")
S3=input("Введите название 3 файла:")
f3=open(S3,"w")
a=f1.read()
b=f2.read()
a=a.split()
b=b.split()
c=a+b
d=[]
for i in range(len(c)):
    d.append(int(c[i]))
d.sort()
c=[]
for i in range(len(d)):
    c.append(str(d[i]))
c=' '.join(c)
f3.write(c)
f1,f2,f3.close()

#22
print('#22')
S1=input("Введите название файла:")
f1=open(S1,"r")
a=f1.read()
f1.close()
f1=open(S1,"w")
for i in range(len(a)):
    if a[i]==' ':
        a=a[:i]
        break
f1.write(a)
f1.close()

#23
print('#23')
S1=input("Введите название файла:")
f1=open(S1,"r")
k=0
for i in f1.readlines():
    a=i.split('/')
    if k==0 and (a[1]=='03' or a[1]=='04' or a[1]=='05'):
        b=i
        k+=1
    elif a[1]=='03' or a[1]=='04' or a[1]=='05':
        if int(a[2])<int(b.split('/')[2]):
            b=i
        elif a[2]==b.split('/')[2]:
            if int(a[1])<int(b.split('/')[1]):
                b=i
            elif int(a[1])==int(b.split('/')[1]):
                if int(a[0]) < int(b.split('/')[0]):
                    b = i
print(b)
f1.close()

#24
print('#24')
S1=input("Введите название файла:")
f1=open(S1,"r")
S2=input("Введите название нового файла:")
f2=open(S2,"w")
for i in f1.readlines():
    a=i.split('/')
    if a[1]=='12' or a[1]=='01' or a[1]=='02':
        f2.write(i)
f1,f2.close()
