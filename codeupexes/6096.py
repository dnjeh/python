d = [[int(0) for j in range(20)] for i in range(20)]
for i in range(19):
    d[i]=input().split()
    for j in range(19):
        d[i][j]=int(d[i][j])
n=int(input())
for i in range(n):
    t=input().split()
    t[0]=int(t[0])-1
    t[1]=int(t[1])-1
    for j in range(19):
        d[t[0]][j]=int(not d[t[0]][j])
        d[j][t[1]]=int(not d[j][t[1]])
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()