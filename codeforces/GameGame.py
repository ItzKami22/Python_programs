a=int(input())
B=[0]*5
C=[]
for i in range(a):
    b=int(input())
    A = [int(i) for i in input().split()]
    for q in range(len(A)):
        while A[q]!=0:
            C.append(str(A[q]%2))
            A[q]=A[q]//2
        C.reverse()
        С=''.join(C)
        B[q]=C
        C=[]
print(B)