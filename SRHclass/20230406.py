import random
print(random.random())
print(random.randrange(1, 7))
print(random.randint(1, 6))
print(random.choice([10, 20, 30]))

import random
import random
time=random.randint(1,24)
issunny=True if random.randint(0, 1)==1 else False
if time>=12:
  print("좋은 오후입니다.", end='')
else:
  print("좋은 아침입니다.", end='')
print("지금 시각은", time, "시 입니다.")
if issunny:
  print("현재 날씨가 화창합니다.")
  print("종달새가 노래한다. & * *")
else:
  print("현재 날씨가 화창하지 않습니다.")
  print("종달새가 노래하지 않는다 . .")

x = 0
while x<3:
  print("안녕하세요.")
  x+=1

student = 1
while student<=3:
  print(student, "번 학생의 성적을 처리한다.")
  student+=1

a=int(input("원하는 단은? "))
i=1
while i<=9:
  print("%d * %d = %d"%(a, i, a*i))
  i+=1

num = 1
sum = 0
while num<=10:
  sum+=num
  print("num의 값 : %d => 합계 : %d"%(num, sum))
  num+=1

i=150
sum=0
while i<=300:
  if i%2==1:
    sum+=i
  i+=1
print("sum =", sum)

i=-5
print("---------------\n  섭씨   화씨  \n---------------")
while i<=5:
  print("%4d%9.1f"%(i, i*9/5.0+32))
  i+=1
print("---------------")

i=1
sumsum=1
while i<=10:
  sumsum*=i
  i+=1
print("10! =", sumsum)

i=1
while i<=20:
  if i%2==0:
    print(i, end=' ')
  i+=1

i=10
while i<=50:
  if(i%3!=0):
    print(i, end=' ')
  i+=1

pw=input("암호 입력 :")
while(pw!="python"):
  pw=input("암호 입력 :")
print("로그인 성공")

import random
cnt=0
guess=-1
answer=random.randint(1, 100)
print("정답 :", answer)
print("1부터 100사이의 숫자를 맞추기")
while guess!=answer:
  guess=int(input("숫자를 맞춰 보세요 : "))
  if answer>guess:
    print("낮음")
  else:
    print("높음")
  cnt+=1
print("축하합니다. 시도횟수 = ", cnt)

