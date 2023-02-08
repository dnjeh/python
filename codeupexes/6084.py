a=input().split()
b=1
for i in range(0, 4):
    b*=int(a[i])
c=b/8/1024/1024
print(float(format(c, ".1f")), "MB")