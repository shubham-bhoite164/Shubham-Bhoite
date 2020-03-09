n=int(input())
a=list(map(int,input().split()))
def rs(a):
    p=a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=p
    return a
def ls(a):
    p=a[0]
    for i in range(1,len(a)):
        t=a[i-1]
        a[i-1]=a[i]
    a[len(a)-1]=p
    return a
def ad(a,x,y):
    s=0
    for i in range(x,y+1):
        s=s+a[i]
    print(s)
for i in range(n):
    b=list(map(int,input().split()))
    if(len(b)==3):
        ad(a,b[1],b[2])
    else:
        if(b[0]==1):
            for k in range(b[1]):
                a=rs(a)
        if(b[0]==2):
            for k in range(b[1]):
                a=ls(a)
        print(*a)
    
