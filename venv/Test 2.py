# 31
print('#31')
M=int(input())
A = [[0] * M for i in range(M)]
for i in range(M):
    s = input()
    s = s.split(' ')
    for j in range(M):
        A[i][j] = int(s[j])
for i in range(M//2):
    for j in range(i):
        A[j][i]=0
for i in range(M//2,M):
    for j in range(M-i-1):
        A[j][i] = 0
for i in range(M):
    print(*A[i])