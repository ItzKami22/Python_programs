#1
print('#1')
c = input("Введите символ С:")
print('Ответ:', ord(c))
print()

#2
print('#2')
n = int(input("Введите число N:"))
print('Ответ:', chr(n))
print()

#3
print('#3')
c = input("Введите символ С:")
print('Ответ:', chr(ord(c) - 1), chr(ord(c) + 1))
print()

#4
print('#4')
n = int(input("Введите число N (1 ≤ N ≤ 26):"))
for i in range(65, 65 + n):
    print(chr(i))
print()

#5
print('#5')
n = int(input("Введите число N (1 ≤ N ≤ 26):"))
for i in range(122, 122 - n, -1):
    print(chr(i))
print()

#6
print('#6')
c = input("Введите символ С:")
print("log >>", ord(c))
if 48 <= ord(c) <= 57:
    print('Ответ:', "digit")
elif 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
    print('Ответ:', "lat")
elif 1040 <= ord(c) <= 1105 or 1025 == ord(c):
    print('Ответ:', "rus")
else:
    print("Invalid character entered")
print()

#7
print('#7')
c = input("Введите строку:")
print('Ответ:', ord(c[1]), ord(c[-1]))
print()

#8
print('#8')
n = int(input("Введите число N:"))
c = input("Введите символ С:")
print('Ответ:', n * c)
print()

#9
print('#9')
print('Задача 9. Вывести строку, содержащую те же символы, но расположенные в обратном порядке.')
c = input("Введите строку:")
s = c[::-1]
print('Ответ:', s)
print()

#10
print('#10')
s = input("Введите строку:")
print('Ответ:')
print(*s, sep=' ')
print()

#11
print('#11')
s = input("Введите строку:")
n = int(input("Введите число N:"))
n = '*' * n
print('Ответ:', n.join(s))
print()

#12
print('#12')
s = input("Введите строку:")
x = len([i for i in s if i.isdigit()])
print('Ответ:')
print(x if x else '0')
print()

#13
print('#13')
s = input("Введите строку:")
x = len([i for i in s if i.isalpha() and i.isupper()])
print('Ответ:')
print(x if x else '0')
print()

#14
print('#14')
s = input("Введите строку:")
x = len([i for i in s if i.isalpha() and i.islower()])
print('Ответ:')
print(x if x else '0')
print()

#15
print('#15')
s = input("Введите строку:")
print('Ответ:', s.lower())
print()

#16
print('#16')
s = input("Введите строку:")
x = ""
for i in s:
    if i.islower():
        x = x + i.upper()
    else:
        x = x + i.lower()
print('Ответ:', x)
print()

#17
print('#17')
s = input("Введите строку:")
if [i for i in s if i == "."]:
    print(2)
elif s.isdigit():
    print(1)
else:
    print(0)

#18
print('#18')
s = input("Введите строку:")
a = -1
k = -1
b = int(s[0])

for i in s[1: len(s)]:
    if i.isdigit():
        a = int(i)
    if not i.isdigit():
        if i == "-":
            k = 0
        elif i == "+":
            k = 1
    if k != -1 and a != -1:
        if k == 0:
            b -= a
        elif k == 1:
            b += a
        a = -1
print('Ответ:', b)
print()

#19
print('#19')
s = input("Введите строку:")
n = int(input("Введите число N:"))
if len(s) > n:
    k = s[len(s) - n:len(s)]
elif len(s) < n:
    k = "." * (n - len(s)) + s
print('Ответ:', k)
print()

#20
print('#20')
s1 = input("Введите строку S1:")
s2 = input("Введите строку S2:")
n1 = int(input("Введите число N1:"))
n2 = int(input("Введите число N2"))
t = s1[:n1] + s2[n2:]
print('Ответ:', t)
print()

#21
print('#21')
s = input("Введите строку:")
c = input("Введите символ:")
k = ""
for i in s:
    if i != c:
        k += i
    else:
        k += i * 2
print('Ответ:', k)
print()

#22
print('#22')
s = input("Введите строку S:")
s0 = input("Введите строку S0:")
c = input("Введите символ:")
k = ""
for i in s:
    if i != c:
        k += i
    else:
        k += s0 + i
print('Ответ:', k)
print()

#23
print('#23')
s = input("Введите строку S:")
s0 = input("Введите строку S0:")
k = ""
for i in s:
    if i != c:
        k += i
    else:
        k += i + s0
print('Ответ:', k)
print()

#24
print('#24')
s = input("Введите строку S:")
s0 = input("Введите строку S0:")
print('Ответ:', s.find(s0) != -1)
print()


