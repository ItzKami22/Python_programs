a,b=map(int,input().split())
A=[]
count2=0
str=0
sto=0
st=0
count3=0
count4=0

for i in range(a):
    A.append(list(map(int,input().split())))
min=A[0][0]
for i in range(a):
    for r in range(b):
        if A[i][r]<min:
            min=A[i][r]
            str=i
            sto=r

    for r in range(b):
        if A[i][r] == min:
            for s in range(a):
                if A[s][r] > min:
                    count4 += 1
            if count4 == 0:
                    print(i + 1, r + 1)
                    count3 += 1
        count4=0
    st += 1
    if i != a - 1:
        min = A[st][0]
        str = st
        sto = 0
    if i == a - 1 and count3 == 0:
        print(0)



