d=int(input())
for i in range(d):
    a, b = map(int, input().split())
    if a%2==0 and b%2!=0:
        print('NO')
    elif a%2==0 and b%2==0:
        if b*b<=a:
            print('YES')
        else:
            print('NO')
    elif a%2!=0 and b%2==0:
        print('NO')
    else:
        if b*b<=a:
            print('YES')
        else:
            print('NO')