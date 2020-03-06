a=list(map(int,input().split()))
k=a[len(a)-1]
b=[]
b.append(k)
for i in range(0,len(a)-1):
    b.append(a[i])
print(*b)

