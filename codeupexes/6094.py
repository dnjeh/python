n=int(input())
a=input().split()
min=0
for i in range(n):
    if min>int(a[i]) or i==0:
        min=int(a[i])
print(min)