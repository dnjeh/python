for dan in range(2, 10):
    print(dan, "단")
    for hang in range(1, 10):
        print(dan, "*", hang, "=", dan*hang)
    print()

dan=2
hang=1
while dan<=9:
    print(dan, "단")
    hang=1
    while hang<=9:
        print(dan, "*", hang, "=", dan*hang)
        hang+=1
    print()
    dan+=1

for i in range(1, 6):
  for j in range(6):
    print('*' if 6-j<=i else ' ', end='')
  print()


a=int(input("수 입력 : "))
cnt=0
for i in range(2, a+1):
  ff=1
  for j in range(2, i):
    if i%j==0:
      ff=0
      break
  if ff==1:
    print("%5d"%(i), end='')
    cnt+=1
    if cnt%5==0:
      print()

price = [500, 5000, 8900, 1800, 2500]
fruit = ["사과", "파인애플", "수박"]
print(price, end='')
print(type(price))
print(fruit, end=' ')
print(type(fruit))

fruitprice = ["사과", 1500, "수박", 8900]
print(fruitprice)
print(type(fruitprice[0]), end = ' ')
print(type(fruitprice[1]), end = ' ')
print(type(fruitprice[2]), end = ' ')
print(type(fruitprice[3]), end = ' ')

a = []
b = list() 
print(type(a), end='')
print(type(b))

num = list(range(1, 21, 2))
print(num)
print(type(num))
a = list("Korea")
print(a)
print(type(a))

print(len(num))
print(len(a))