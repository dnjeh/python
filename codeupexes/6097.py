hw=input().split()
d = [[0 for j in range(int(hw[1]))] for i in range(int(hw[0]))]
n=int(input())
for i in range(n):
    t=input().split()
    for j in range(int(t[0])):
        if(int(t[1])):
            d[j+int(t[2])-1][int(t[3])-1]=1
        else:
            d[int(t[2])-1][j+int(t[3])-1]=1
for i in range(int(hw[0])):
    for j in range(int(hw[1])):
        print(d[i][j], end=' ')
    print()