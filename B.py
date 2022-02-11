#n = int(input())
#a=[]
i=int()
j=int()
max=int()
#if n==0:
#    exit()

#while len(a)<n:
#    a.append(input())

while i<n:
    while j<n:
        max=int(a[i])*int(a[j])
        if max<int(a[i])*int(a[j]):
            max=int(a[i])*int(a[j])
        j=j+1
    i=i+1

print(max)
