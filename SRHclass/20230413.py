for i in [1, 2, 3]:
  print("안녕하세요")

for i in range(10):
  print(i, end=' ')

for i in range(1, 11):
  print(i, end=' ')

for i in range(1, 10, 2):
  print(i, end=' ')

for i in range(20, 0, -2):
  print(i, end=' ')

for i in range(3):
  print("안녕하세요")

a=10
for num in range(1, 5, 2):
  a+=num
print(a)

for i in range(3):
  print("%d 번째 학생의 성적처리"%(i+1))

for i in range(2, 21, 2):
  print(i, end=' ')

for i in range(9):
  print("2 x %d = %d"%(i+1, (i+1)*2))

sum=0
for i in range(2, 101, 2):
  sum+=i
print("sum =", sum)

cnt=1
for i in range(1, 11):
  cnt*=i
print("10! =", cnt)

sum=5
for i in range(3):
  for j in range(7 if i<=1 else 6):
    print(sum, end=' ')
    sum+=5
  print()

a=int(input("정수를 입력하시오: "))
for i in range(1, a+1):
  if a%i==0:
    print(i, end=' ')

first=0
second=1
third=1
for i in range(20):
  print(first, end=' ')
  first=second
  second=third
  third=first+second

for i in range(1, 41):
  print('-' if i%10 else '+', end='')

i=1
while i<=40:
  print('-' if i%10 else '+', end='')
  i+=1

for i in range(1, 41):
  print('-' if i%10!=5 else '+', end='')

print("----------------------------------------\n 센치(cm) 인치(inch) 피트(ft) 야드(yd)\n----------------------------------------")
for cm in range(10, 101, 10):
  inch=cm*0.393701
  ft=cm*0.032808
  yd=cm*0.010936
  print("%6d%10.1f%10.1f%10.1f"%(cm, inch, ft, yd))
print("----------------------------------------")

for i in range(1, 1001):
  print(i, end=' ')
  if i==10:
    break

score = [92, 86, 68, 120, 56, 72]
for s in score:
  if s<0 or s>100:
    break
  print(s)
print("성적 처리 끝")

score = [92, 86, 68, 120, 56, 72]
for s in score:
  if s<0 or s>100:
    continue
  print(s)
print("성적 처리 끝")

import random
a, b = random.randint(1, 100000), random.randint(1, 100000)
print("%d+%d?"%(a, b))
while True:
  c=int(input("정답을 입력하세요.: "))
  if(c==a+b):
    break
print("참 잘했어요")

while True:
  light=input("신호등 색상 입력 : ")
  if(light=="green"):
    break
print("길을 건너세요")

i=0
sum=0
while True:
  if(sum>50):
    break
  i+=1
  sum+=i
print("합이 50보다 커지는 수는 %d이고 합은 %d다."%(i, sum))

