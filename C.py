N=int(input())
i=0
j=0
a=[[],[]]

while i<N:
    a[0].append(i)
    i=i+1
    while j<N:
        a[i].append(j)
        j=j+1

print (a)
