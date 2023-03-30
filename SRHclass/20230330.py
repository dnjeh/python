x=int(input("숫자입력:"))
if x > 10 and x % 2 == 0:
  print("10 초과 짝수")

a=int(input("필기 성적을 입력하세요: "))
b=int(input("실기 성적을 입력하세요: "))
if a<80 or b<80:
  print("불", end='')
print("합격!")

a=int(input("몇 살이세요?: "))
print("입장료는", "무료" if 65<=a or 0>=a and a<7 else "3000원", "입니다.") #0>=a<7

age=int(input("나이 : "))
height=int(input("키 :"))
print("놀이기구를 탈 수 ", end='')
if age>=10 and height >= 150:
  print("있다")
else:
  print("없다")

id = input("아이디를 입력하세요: ")
user_level = int(input("회원  레벨을 입력하세요.: "))
print("관리자", end='')
if id=="admin" or user_level==1:
  print("입니다.")
else:
  print("가 아닙니다.")

a=int(input("정수를 입력하세요: "))
print(a,"은(는) 1~100사이에 ", "있다" if a<=100 and a>=1 else "없다.", sep='')

a = int(input("몇 월?"))
if 3<=a<=5:
  print("봄")
elif 6<=a<=8:
  print("여름")
elif 9<=a<=11:
  print("가을")
else:
  print("겨울")

a=int(input("구매금액: "))
if a<20000:
  print("새벽 배송이 불가능합니다.")
elif a<50000:
  print("배송비 2500원이 추가됩니다.")
else:
  print("무료배송입니다.")

a=int(input("점수를 입력하세요: "))
if a>=90:
  print("A 등급입니다.")
elif a>=80:
  print("B 등급입니다.")
elif a>=80:
  print("C 등급입니다.")
else:
  print("F 등급입니다.")

a=int(input("첫 번째 수: "))
b=int(input("두 번째 수: "))
c=int(input("세 번째 수: "))
print("가장 큰 수는", a if a>=b and a>=c else (b if b>=a and b>=c else c), "입니다.")

a=int(input("온도를 입력하세요: "))
if a<0:
  print("물의 상태는 고체입니다.")
elif a<100:
  print("물의 상태는 액체입니다.")
else:
  print("물의 상태는 기체입니다.")

a=int(input("영어시험 점수를 입력하세요 : "))
b=int(input("수학시험 점수를 입력하세요 : "))
if a>=80 and b>=80:
  print("합격")
elif a>=80 or b>=80:
  print("재시험 기회제공")
else:
  print("불합격")

a=int(input("  1: 매우만족  2: 만족    3: 불만족\n서비스가 어떠셨나요(예: 1 또는 2 또는 3) : "))
b=int(input("음식값을 입력해 주세요(예:8000) : "))
print("\n팁 :", end='')
if a==1:
  print(b*1/4, "원")
elif a==2:
  print(b*1/10, "원")
else:
  print(b*1/20, "원")

a=int(input("물건 구매가를 입력하세요 : "))
print("구매가 :", a, "원")
print("할인율 :", end='')
if a>=10000 and a<50000:
  print("5%")
  b=a*5/100
elif a<300000:
  print("7.5%")
  b=a*75/1000
else:
  print("10%")
  b=a*10/100
print("할인 금액 :", b, "원\n지불 금액 :", a-b, "원")

a=int(input("원하는 메뉴를 선택하세요.\n1. 떡볶이 3000원\n2. 김밥 2500원\n3. 튀김 3500원\n번호 선택 : "))
if a==1:
  b=int(input("당신은 떡볶이를 선택하셨군요!\n떡볶이를 몇 인분 주문하시겠습니까? "))
  print("총 가격은", b*3000,"원 입니다.")
elif a==2:
  b=int(input("당신은 김밥를 선택하셨군요!\n김밥를 몇 인분 주문하시겠습니까? "))
  print("총 가격은", b*2500,"원 입니다.")
elif a==3:
  b=int(input("당신은 튀김을 선택하셨군요!\n튀김를 몇 인분 주문하시겠습니까? "))
  print("총 가격은", b*3500,"원 입니다.")
else:
  print("1, 2, 3 중 하나를 선택해주세요")

a=int(input("체중을 입력하세요: "))
b=float(input("키를 입력하세요(m): "))
c=a/b**2
if 0<=c<=15:
  print("당신의 bmi지수는", c, "이며 정상입니다")
elif c<=25:
  print("당신의 bmi지수는", c, "이며 과체중입니다")
else:
  print("당신의 bmi지수는", c, "이며 비만입니다")

a=int(input("체중을 입력하세요: "))
b=int(input("키을 입력하세요(cm): "))
c=int(input("나이를 입력하세요: "))
d=input("성별을 입력하세요: 남자/여자 : ")
if d=="남자":
  print("당신의 기초대사량은", 66.47+(13.75*a) + (5*b) - (6.76*c), "입니다.")
else:
  print("당신의 기초대사량은", 655.1+(9.56*a) + (1.85*b) - (4.68*c), "입니다.")

x=17
if x>10:
  if x%2==0:
    print("10초과 짝수")
  else:
    print("10초과 홀수")
else:
  print("10이하")

userid=input("아이디를 입력하세요 : ")
user_level=int(input("회원 레벨을 입력해주세요 : "))
if userid=="admin":
  print("모든 콘텐츠 이용 가능")
else:
  if 2<=user_level<=7:
    print("일부 콘텐츠 이용 가능")
  else:
    print("모든 콘텐츠 이용 불가능")

ny=int(input("현재년을 입력해 주세요 : "))
nm=int(input("현재월을 입력해 주세요 : "))
nd=int(input("현재일을 입력해 주세요 : "))
by=int(input("출생년을 입력해 주세요 : "))
bm=int(input("출생월을 입력해 주세요 : "))
bd=int(input("출생일을 입력해 주세요 : "))
#print("--------------------------------------------\n오늘 날짜 :", ny, "년", nm, "월", nd, "일\n생년 월일 :", by, "년", bm, "월", bd, "일\n--------------------------------------------\n만 나이 :", end='')
print("--------------------------------------------\n오늘 날짜 :%d년 %d월 %d일\n생년 월일 : %d년 %d월 %d일\n--------------------------------------------\n만 나이 :"%(ny, nm, nd, by, bm, bd), end='')
if bm<nm:
  print(ny-by, "세")
elif bm==nm:
  if bd<nd:
    print(ny-by, "세")
  else:
    print(ny-by-1, "세")
else:
  print(ny-by-1, "세")

import datetime
from pytz import timezone
now = datetime.datetime.now(timezone("Asia/Seoul"))
print(now)

import datetime
from pytz import timezone

import datetime
from pytz import timezone

now = datetime.datetime.now(timezone("Asia/Seoul"))
a=now.hour
if a>=13:
  print("현재 시각, %d시는 오후입니다."%(a))
else:
  print("현재 시각, %d시는 오전입니다."%(a))
  
now = datetime.datetime.now(timezone("Asia/Seoul"))
a=now.month
if 3<=a<=5:
  c="봄"
elif 3<=a<=5:
  c="여름"
elif 3<=a<=5:
  c="가을"
else:
  c="겨울"
print("이번 달은 %d월로 %s입니다!"%(a, c))