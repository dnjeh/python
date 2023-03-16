price = int(input("가격을 입력하세요 : "))
num = int(input("개수를 입력하세요 : "))
sum = price * num
print("총액은", sum, "원입니다.")

width = int(input("사각형의 가로 : "))
height = int(input("사각형의 세로 : "))
sum = width * height
print("사각형의 면적은",sum, "입니다")

name = input("이름? ")
year = int(input("태어난 해는? "))
age = 2023 - year + 1
print(name, "님의 나이는",age,"세 입니다.")

price = int(input("물건의 가격?: "))
num = int(input("물건 구매 개수?: "))
given = int(input("지불한 돈?: "))
print("거스름돈은", given-(price*num), "원입니다.")

print(type("안녕하세요"))
print(type(273))
print(type(3.1415926535))

score = 100
print(score)
print(type(score))

score = "high"
print(score)
print(type(score))

num = 123456789
print(num)
print(type(num))

num = -20909
print(num)
print(type(num))

a = 1.5
b = -3.5
print(a, b)
print(type(a), type(b))

x = 3.3764
y = 6/2
print(x, y)
print(type(a), type(b))

a = "Korea 서울 1234"
print(a)
print(type(a))

a = 30
print(a)
print(type(a))
b='30'
print(b)
print(type(b))

print('I say "hello" to you')
print("Let's go")

a = 5
b = a==5
print(b)

if a==5:
  print("a는 5")

a = input("첫번째숫자를입력하세요: ")
b = input("두번째숫자를입력하세요: ")
c = a + b
print(c)

a = input("첫번째숫자를입력하세요: ")
b = input("두번째숫자를입력하세요: ")
c = int(a) + int(b)
print(c)

inch = float(input("인치를 입력하세요 : "))
print("센치미터:", inch*2.54, "cm")

a=int(input("반지름은? : "))
print("반지름이", a, "인 원의 둘레는", a*2*3.14, "이고, 면적은", a*3.14*3.14)

a=int(input("현재 키는? "))
b=int(input("5개월 후의 목표 키는? "))
print("한달에", (b-a)/5, "씩 성장해 보세요!")

book=int(input("책 값 : "))
discount=float(input("할인율(%) : "))
delivery=int(input("배송비: "))
print("결재하실 금액은", book/100*(100-discount)+delivery, "원 입니다.")

o=int(input("첫 번째 과목: "))
t=int(input("두 번째 과목: "))
print("합계:", o+t, ", 평균:", (o+t)/2)

a=int(input("삼각형의 밑변 길이 : "))
b=int(input("삼각형의 높이 : "))
print("삼각형의 면적 :", a*b/2)

kg=float(input("킬로그램(kg) 입력: "))
print(kg, "kg은", kg*2.2046, "파운드입니다.")