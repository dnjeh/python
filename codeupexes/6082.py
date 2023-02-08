n=int(input())
for i in range(1, n+1):
    print(i if i%10!=3 and i%10!=6 and i%10!=9 else 'X', end=' ')