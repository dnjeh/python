print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)
print(5%2)

x = 10 % 3
print(x)
y = 7//3
print(y)

a = 10
b = 20
c = a + b * 10 - 5 / 5
print(c)

x = 2**3
print(x)
y = 10**4
print(y)

hello = "안녕" * 5
print(hello)

s1 = "대한민국"
s2 = "만세"
print(s1+s2)
print(s1*5)

print("korea"+str(2021))
print(10+int("22"))
print(10 + int(22.5))
print(10 + int(float(22.5)))
#print("korea"+2021)

x = 10
x += 20
print(x)

a = 5
a = a + 1
print(a)
a = 5
a += 1
print(a)
a -= 5
print(a)
a *= 2
print(a)

x = 3
y = 5
x *= x + y
print(x)

money=int(input("투입한 돈: "))
price=int(input("물건 값: "))
change=money-price
print("거스름돈:", change)
print("500원 동전의 개수:", change//500)
print("100원 동전의 개수:", change%500//100)

if 3 < 5:
  print("Hello World")
if 3 > 5:
  print("Hello World")

age = int(input("몇살입니까?"))
if age<20:
  print("학생입니다.")

age = 20
if age < 20:
  print("학생입니다")
print("안녕히가세요.")

print( 3 == 5 )
print( 3 != 5 )
print( 3 < 5 )

x = 4
print( 1 < x < 5 )

#print( 3 => 5 )

a=int(input("숫자입력: "))
if a<5:
  print("5보다 작다.")
elif a>5:
  print("5보다 크다.")
else:
  print("5이다.")

country = input("나라 입력: ")
if country == "Korea":
  print("한국")

age = int(input("몇살입니까? "))
if age < 20:
  print("학생입니다.")
else:
  print("성인입니다.")

a=int(input("숫자입력: "))
if a % 2:
  print("홀수")
else:
  print("짝수")

a=int(input("정수입력: "))
if a % 5:
  print("5의 배수가 아닙니다.")
else:
  print("5의 배수 입니다.")

password = input("암호입력")
if password == "암호":
  print("암호이다.")
else:
  print("암호가 아니다.")

a=int(input("숫자를 입력하세요: "))
if a>0:
  print("양수입니다.")
else:
  print("0 또는 음수입니다.")

a = int(input("첫번째 숫자를 입력하세요:"))
b = int(input("두번째 숫자를 입력하세요:"))
if a>b:
  print(a-b)
else:
  print(b-a)

a = int(input("1(주간 근무) 또는 2(야간근무)을 입력해주세요 : "))
b = int(input("근무 시간을 입력해주세요 : "))
print(b, "시간 동안 일한", end=' ')
if a-1:
  print("야간 급여는", b*9500*3//2, "원 입니다.")
else:
  print("주간 급여는", b*9500, "원 입니다.")

a=input("이름을 입력하세요: ")
b=int(input("일주일간 일한 시간을 입력하세요: "))
if b>40:
  print("초과 시간:", b-40)
  print(a, "님의 주급은", 40*12000+(b-40)*12000*3//2, "입니다.")
else:
  print(a, "님의 주급은", b*12000, "입니다.")

print((3==3) and (4!=3))
print((3==3) or (4!=3))
print(not (4!=3))

