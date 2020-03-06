a=list(map(int,input().split()))
c=[]
for i in range(1):
    d=i
    b=[0]*len(a)
    k=0
    s=0
    for i in range(d,len(a)):
        b[k]=a[i]
        k=k+1
    for i in range(d):
        b[k]=a[i]
        k=k+1
    for i in range(len(b)):
        s=s+b[i]*i
    c.append(s)
print(max(c))

