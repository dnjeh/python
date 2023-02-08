a=input().split()
for i in range(0, 3):
    a[i]=int(a[i])
i=1
while (i%a[0] or i%a[1] or i%a[2]):
    i+=1
print(i)