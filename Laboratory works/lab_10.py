#1
print('#1')
s = input("Введите строку S:")
s0 = input("Введите строку S0:")
print('Ответ:', s.count(s0))
print()

#2
print('#2')
s = input("Введите строку S:")
s0 = input("Введите строку S0:")
k = s.find(s0)
S = s[0:k] + s[k + len(s0):len(s)]
print('Ответ:', S)
print()

#3
print('#3')
s = input("Введите строку S:")
s1 = input("Введите строку S1:")
s2 = input("Введите строку S2:")
r = s.rfind(s1)
S = s[0:r] + s2 + s[r+len(s1):len(s)]
print('Ответ:', S)
print()

#4
print('#4')
s = input("Введите строку S:")
b=s
l = s.find(' ')
b=b[:l]+b[l+1:]
r = b.find(' ')
S = s[l:r+1]
print('Ответ:', S)
print()

#5
print('#5')
s = input("Введите строку S:")
l = s.find(' ')
r = s.rfind(' ')
S = s[l:r]
print('Ответ:', S)
print()

#6
print('#6')
s = input("Введите строку S:")
k = 1
l=0
for i in s:
    if i == ' ' and l==0:
        k += 1
        l+=1
    elif i!=' ':
        l=0
print('Ответ:', k)
print()

#7
print('#7')
s0 = input("Введите строку S:")
s = s0 + ' '
spase = True
s1 = ''
amt = 0
for i in s:
    if i != ' ':
        s1 += i
        spase = True
    elif spase:
        if s1[0] == s1[len(s1) - 1]:
            amt += 1
        s1 = ''
        spase = False
print('Ответ:', amt)
print()

#8
print('#8')
s0 = input("Введите строку S:")
s = s0 + ' '
spase = True
s1 = ''
amt = 0
for i in s:
    if i != ' ':
        s1 += i
        spase = True
    elif spase:
        if s1.find('А') != -1:
            amt += 1
        s1 = ''
        spase = False
print('Ответ:', amt)
print()

#9
print('#9')
s = input("Введите строку S:")
tag = -1
while s.find('  ') != -1:
    tag = s.find("  ")
    if tag != -1:
        s = s[0:tag] + s[tag + 1:len(s)]
print('Ответ:', s)
print()

#10
print('#10')
s0 = input("Введите строку S:")
s = s0 + ' '
spase = True
s1 = ''
short = 100
for i in s:
    if i != ' ':
        s1 += i
        spase = True
    elif spase:
        if len(s1) < short:
            short = len(s1)
        s1 = ''
        spase = False
print('Ответ:', short)
print()

#11
print('#11')
s = input('Введите строку S: ')


def point(string, index, char):
    return string[:index] + char + string[index + 1:]


li = s.split(' ')
s1 = ""
for i in range(0, len(li)):
    if (li[i] != ''):
        char1 = (li[i])[0]
        for j in li[i]:
            for k in range(1, (li[i]).count(char1)):
                li[i] = point(li[i], (li[i]).rfind(char1), ".")
        if (li[i] != ''):
            s1 += li[i] + ' '
print('Ответ:', s1)
print()

#12
print('#12')
s = input('Введите строку S: ')
li = s.split(' ')
li.sort()
s1 = ""
for i in li:
    if (i != ''):
        s1 += i + ' '
print(s1)
print()

#13
print('#13')
s = input('Введите строку S: ')
sum = len([x for x in s if x in ',.!?'])
print('Ответ:', sum)
print()

#14
print('#14')
s = input('Введите строку S: ')
sum = len([x for x in s if x in 'аеёиоуэюяАЕЁИОУЭЮЯ'])
print('Ответ:', sum)
print()

#15
print('#15')
s = input('Введите строку S: ')
tag = s.rfind("\\")
point = s.rfind(".")
print('Ответ:', s[tag + 1:point])
print()

#16
print('#16')
s = input('Введите строку S: ')
point = s.rfind(".")
print('Ответ:', s[point + 1:])
print()

#17
print('#17')
s = input('Введите строку S:')
li = s.split("\\")
if len(li) != 2:
    o =li[1]
else:
    o = "\\"
print('Ответ:', o)
print()

# 18
print('#18')
s = input('Введите строку S:')
for i in range(len(s)):
    if s[i] == "Я":
        s = s[:i] + "А" + s[i + 1:]
    elif s[i] == "я":
        s = s[:i] + "а" + s[i + 1:]
    elif ord(s[i]) == 175:
        s = s[:i] + "р" + s[i + 1:]
    else:
        s = s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]
print(s)
print()

# 19
print('#19')
s = input('Введите строку S:')
K = int(input())
for i in range(len(s)):
    if ord(s[i])>=1072:
        if ord(s[i])+K<=1103:
            s = s[:i] + chr(ord(s[i]) + K) + s[i + 1:]
        else:
            s = s[:i] + chr((ord(s[i]) + K)-1103+1071) + s[i + 1:]
    else:
        if ord(s[i])+K<=1071:
            s = s[:i] + chr(ord(s[i]) + K) + s[i + 1:]
        else:
            s = s[:i] + chr((ord(s[i]) + K)-1071+1039) + s[i + 1:]

print(s)
print()

# 20
print('#20')
s = input('Введите строку S:')
K = int(input())
for i in range(len(s)):
    if ord(s[i])>=1072:
        if ord(s[i])-K>=1072:
            s = s[:i] + chr(ord(s[i]) - K) + s[i + 1:]
        else:
            s = s[:i] + chr(1103-(K-((ord(s[i])-1071)))) + s[i + 1:]
    else:
        if ord(s[i])-K>=1040:
            s = s[:i] + chr(ord(s[i]) - K) + s[i + 1:]
        else:
            s = s[:i] + chr(1103-(K-((ord(s[i])-1071)))) + s[i + 1:]
print(s)
print()


# 21
print('#21')
s = input('Введите строку S:')
k=0
l=0
z=0
p=0
c=0
for i in range(len(s)):
    if s[i]=="(" and k==0:
        k=1
        c+=1
    if s[i]=="[" and l==0:
        l=1
        c += 1
    if s[i]=="{" and z==0:
        z=1
        c += 1
    if k==1 and (s[i]=="]" or s[i]=="}") and c==0:
        print(i)
        p=1
        break
    elif k==1 and (s[i]=="{" or s[i]=="[" or s[i]=="(") and c==0:
        print(-1)
        p=1
        break
    if l==1 and (s[i]==")" or s[i]=="}") and c==0:
        print(i)
        p=1
        break
    elif l==1 and (s[i]=="{" or s[i]=="[" or s[i]=="(") and c==0:
        print(-1)
        p=1
        break
    if z==1 and (s[i]=="]" or s[i]==")") and c==0:
        print(i)
        p=1
        break
    elif z==1 and (s[i]=="{" or s[i]=="[" or s[i]=="(") and c==0:
        print(-1)
        p=1
        break
    if k==1 and s[i]==")":
        k=0
    if l==1 and s[i]=="]":
        l=0
    if z==1 and s[i]=="}":
        z=0
    c=0
if (z==1 or l==1 or k==1) and p==0:
    print(-1)
elif p==0:
    print(0)