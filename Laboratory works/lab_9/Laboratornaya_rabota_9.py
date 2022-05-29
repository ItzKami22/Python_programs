# 9.1
print('Задача 1. Вывести код символа.')
c = input("Введите символ С:")
print('Ответ:', ord(c))
print()

# 9.2
print('Задача 2. Вывести символ с кодом, равным N.')
n = int(input("Введите число N:"))
print('Ответ:', chr(n))
print()

# 9.3
print('Задача 3. Вывести код символв.')
c = input("Введите символ С:")
print('Ответ:', chr(ord(c) - 1), chr(ord(c) + 1))
print()

# 9.4
print('Задача 4. Вывести N первых прописных букв латинского алфавита.')
n = int(input("Введите число N (1 ≤ N ≤ 26):"))
for i in range(65, 65 + n):
    print(chr(i))
print()

# 9.5
print('Задача 5. Вывести N последних строчных букв латинского алфавита в обратном порядке .')
n = int(input("Введите число N (1 ≤ N ≤ 26):"))
for i in range(122, 122 - n, -1):
    print(chr(i))
print()

# 9.6
# -*- coding: utf8 -*-
print('Задача 6. Вывести код символв.')
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

# 9.7
# -*- coding: utf8 -*-
print('Задача 7. Вывести коды первого и последнего символа.')
c = input("Введите строку:")
print('Ответ:', ord(c[1]), ord(c[-1]))
print()

# 9.8
# -*- coding: utf8 -*-
print('Задача 8. Вывести строку длины N, которая состоит из символов C.')
n = int(input("Введите число N:"))
c = input("Введите символ С:")
print('Ответ:', n * c)
print()

# 9.9
# -*- coding: utf8 -*-
print('Задача 9. Вывести строку, содержащую те же символы, но расположенные в обратном порядке.')
c = input("Введите строку:")
s = c[::-1]
print('Ответ:', s)
print()

# 9.10
# -*- coding: utf8 -*-
print('Задача 10. Вывести строку, содержащую символы строки S с пробелами.')
s = input("Введите строку:")
print('Ответ:')
print(*s, sep=' ')
print()

# 9.11
# -*- coding: utf8 -*-
print('Задача 11. Вывести строку, содержащую символы строки S с *.')
s = input("Введите строку:")
n = int(input("Введите число N:"))
n = '*' * n
print('Ответ:', n.join(s))
print()

# 9.12
# -*- coding: utf8 -*-
print('Задача 12. Подсчитать количество содержащихся в ней цифр.')
s = input("Введите строку:")
x = len([i for i in s if i.isdigit()])
print('Ответ:')
print(x if x else '0')
print()

# 9.13
print('Задача 13. Подсчитать количество прописных латинских букв.')
s = input("Введите строку:")
x = len([i for i in s if i.isalpha() and i.isupper()])
print('Ответ:')
print(x if x else '0')
print()

# 9.14
# -*- coding: utf8 -*-
print('Задача 14. Подсчитать общее количество строчных латинских и русских букв.')
s = input("Введите строку:")
x = len([i for i in s if i.isalpha() and i.islower()])
print('Ответ:')
print(x if x else '0')
print()

# 9.15
# -*- coding: utf8 -*-
print('Задача 15. Преобразовать в ней все прописные латинские буквы в строчные.')
s = input("Введите строку:")
print('Ответ:', s.lower())
print()

# 9.16
# -*- coding: utf8 -*-
print('Задача 16. Преобразовать строчные буквы в прописные, а прописные — в строчные.')
s = input("Введите строку:")
x = ""
for i in s:
    if i.islower():
        x = x + i.upper()
    else:
        x = x + i.lower()
print('Ответ:', x)
print()

# 9.17
# -*- coding: utf8 -*-
print('Задача 17. Определить значение строки.')
s = input("Введите строку:")
if [i for i in s if i == "."]:
    print(2)
elif s.isdigit():
    print(1)
else:
    print(0)

# 9.18
# -*- coding: utf8 -*-
print('Задача 18. Вывести значение выражения.')
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

# 9.19
# -*- coding: utf8 -*-
print('Задача 19. Преобразовать строку S в строку длины N .')
s = input("Введите строку:")
n = int(input("Введите число N:"))
if len(s) > n:
    k = s[len(s) - n:len(s)]
elif len(s) < n:
    k = "." * (n - len(s)) + s
print('Ответ:', k)
print()

# 9.20
# -*- coding: utf8 -*-
print('Задача 20. Получить новую строку.')
s1 = input("Введите строку S1:")
s2 = input("Введите строку S2:")
n1 = int(input("Введите число N1:"))
n2 = int(input("Введите число N2"))
t = s1[:n1] + s2[n2:]
print('Ответ:', t)
print()

# 9.21
# -*- coding: utf8 -*-
print('Задача 21. Удвоить каждое вхождение символа C в строку S.')
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

# 9.22
# -*- coding: utf8 -*-
print('Задача 22. Перед каждым вхождением символа C в строку S вставить строку S0.')
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

# 9.23
# -*- coding: utf8 -*-
print('Задача 23. После каждого вхождения символа C в строку S вставить строку S0.')
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

# 9.24
# -*- coding: utf8 -*-
print('Задача 24. После каждого вхождения символа C в строку S вставить строку S0.')
s = input("Введите строку S:")
s0 = input("Введите строку S0:")
print('Ответ:', s.find(s0) != -1)
print()


