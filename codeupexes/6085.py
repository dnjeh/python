a=input().split()
b=1
for i in range(0, 3):
    b*=int(a[i])
c=b/8/1024/1024
print(format(c, "0.2f"), "MB")