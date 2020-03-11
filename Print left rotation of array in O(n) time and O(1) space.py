a=list(map(int,input().split()))
b=a+[]
n=int(input())
l=len(a)
def rotate(a):
    p=a[0]
    c=[]
    for i in range(1,len(a)):
        c.append(a[i])
    c.append(p)
    return c
for i in range(n):
    k=int(input())
    c=[]
    k=k%5
    a=b+[]
    for i in range(k):
        a=rotate(a)
print(a)
