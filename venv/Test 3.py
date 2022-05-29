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
