a=input()
b=''
for i in range(0,len(a),2):
    if int(a[i])==1:
        if len(b)!=len(a)-1:
            b+="1+"
        else:
            b+="1"
for i in range(0,len(a),2):
    if int(a[i])==2:
        if len(b)!=len(a)-1:
            b+="2+"
        else:
            b+="2"
for i in range(0,len(a),2):
    if int(a[i])==3:
        if len(b)!=len(a)-1:
            b+="3+"
        else:
            b+="3"
print(b)