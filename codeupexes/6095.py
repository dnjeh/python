n=int(input())
d = [[0 for j in range(20)] for i in range(20)]
for i in range(n):
    t=input().split()
    d[int(t[0])-1][int(t[1])-1]=1
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()
print(d)