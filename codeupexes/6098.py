d=[]
for i in range(10):
    d.append([])
x=y=1
for i in range(10):
    d[i]=input().split()
    for j in range(10):
        d[i][j]=int(d[i][j])
while True:
    d[y][x]=9
    if not d[y][x+1]:
        x+=1
    elif not d[y+1][x]:
        y+=1
    elif d[y+1][x]==2 or d[y][x+1]==2:
        if d[y][x+1]==2:
            d[y][x+1]=9
            break
        else:
            d[y+1][x]=9
            break
    else:
        break
for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
