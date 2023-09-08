list = [1, 1]
n = int(input())
for i in range(n):
    t = list[-1]
    list.append(list[t-1]+list[-t])
print(list[n-1])