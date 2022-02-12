n=int(input())
a=[]
i=int()

if n==0:
    exit()

if n%2==0:
    while len(a)<=n:
        a.append('.'*n)
    while i<n:
        a[i] = a[i].replace('.', '#', i+1)
        print(a[i])
        i=i+1
elif n%2!=0:
    while len(a)<=n:
        a.append('#'*n)
    while i<n:
        a[i] = a[i].replace('#', '.', n-i-1)
        print(a[i])
        i=i+1
