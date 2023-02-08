a=input().split()
a[0]=int(a[0])
for i in range(1, int(a[3])):
    a[0]*=int(a[1])
    a[0]+=int(a[2])
print(int(a[0]))