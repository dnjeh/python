score = [88, 95, 70, 100, 99]
score[0]=10
score[1]=20
score[2]=30
score[-2]=40
score[-1]=50
print(score)

animals = ["토끼", "거북이", "사자", "호랑이"]
i=0
while i<4:
  print(animals[i])
  i+=1

nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:5:1])
print(nums[1:7:2])
print(nums[0:5:2])

nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2::1])
print(nums[1::2])
print(nums[0::2])

fruits = ["사과", "오렌지", "딸기", "포도", "감", "키위", "멜론", "수박"]
print(fruits)
print(fruits[0])
print(fruits[1:4])
print(fruits[2:])
print(fruits[-1])
print(fruits[-4:-2])
print(fruits[-3:])

my_list=list("PythonIsFun!")
print(my_list)
print(my_list[5:11])
print(my_list[-5:-2])
print(my_list[:4])
print(my_list[8:])

s = "python"
print(s[2])
print(s[-2])
print(s[1:4])

file = "20210505-104830.jpg";
print("촬영 날짜: "+file[4:6]+"월"+file[6:8]+"일")
print("촬영 시간: "+file[9:11]+"시"+file[11:13]+"분")
print("확장자:"+file[-3:])

s = "차종: 코란도C, 제조사:쌍용, 배기량: 1998"
print(s[14:16])

jumin = "901231-1914983"
year = jumin[0:2]
if int(jumin[7:8])%2==0:
  gender = "여자"
else:
  gender = "남자"
print("{}년생 {}입니다.".format(year, gender))

nums = [1,2,3,4]
nums.append(5)
print(nums)
nums.insert(2, 99)
print(nums)

list1 = [1,2,3,4,5]
list2 = [10, 11]
list1.extend(list2)
print(list1)

score = [88, 95, 70, 100, 99]
print("100의 위치: ", score.index(100)+1)
print(score.pop())
print(score.pop())
print(score.pop(1))
print(score)

score = [88, 95, 70, 100, 99]
score.remove(99)
print("99삭제 후 :", score)
score.sort()
print("리스트 정렬 후:", score)
score.sort(reverse=True)
print("거꾸로 정렬:", score)
score.clear()
print("리스트 삭제:", score)

list1 = ['a', "bb", 'c', 'd', "aaa", 'c', "ddd", "aaa", 'b', "cc", 'd', "aaa"]
length = list1.count("aaa")
print(length)

mylist = ["사과", "바나나", "파인애플"]
mylist.append("키위")
mylist.append("배")
for a in mylist:
  print(a)

scores = []
while True:
  score = int(input("성적을 입력하세요(종료 : -1):"))
  if score == -1:
    break
  else :
    scores.append(score)
print(scores)

num = []
for i in range(5):
  num.append(int(input("숫자입력하세요: ")))
num.sort()
print(num)

emails = [["kim", "naver.com"], ["hwang", "hanmail.net"], ["lee", "korea.com"], ["choi", "gmail.com"]]
email_new = []
for email in emails:
  email_new.append(email[0] + "@" + email[1])
print(email_new)

fruits = ["apple", "orange", "banana"]
for fruit in fruits:
  print(fruit)

s = "Hello"
for i in s:
  print(i, end='')

colors = ["빨간색", "파란색", "노란색", "초록색"]
for color in colors:
  print("나는 {}을 좋아한다".format(color))

numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
sum=0
for number in numbers:
  sum+=number
print("합계 :", sum)

score = [1,3,5,7,9,11,13]
cnt =0
for num in score:
  if num<10:
    cnt+=1
    print(num, end=' ')
print("\n10보다 작은 수의 개수 : ")

questions = ["tr_in", "b_s", "_axi", "air_lane"]
answers = ["a", "u", "t", "p"]
count = 0
for i in range(4):
  q="%s 에서 밑줄(_) 안에 들어갈 알파벳은? "%(questions[i])
  ans = input(q)
  if(ans==answers[i]):
    print("정답입니다!")
    count+=1
  else:
    print("틀렸습니다!")
print("당신의 점수는 {}/4 dlqslek".format(count))

scores = []
for i in range(5):
  scores.append(int(input("성적입력: ")))
sum=0
for score in scores:
  sum+=score
print(scores)
print("총점은 {}이고 평균은 {}입니다.".format(sum, sum/5))

numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
sum=0
i=0
print("짝수 번째 요소 : ", end='')
while i<10:
  if i%2==1:
    print(numbers[i], end=' ')
    sum+=numbers[i]
  i+=1
print("\n합계 : {}".format(sum))

s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87, 87, 36, 82, 98, 84, 76, 63, 69, 53, 22]
soo=0
woo=0
mi=0
yang=0
ga=0
i=0
while i<20:
  if s[i]//10==9 or s[i]//10==10:
    soo+=1
  elif s[i]//10==8:
    woo+=1
  elif s[i]//10==7:
    mi+=1
  elif s[i]//10==6:
    yang+=1
  else:
    ga+=1
  i+=1
print("수 : {}명\n우 : {}명\n미 : {}명\n양 : {}명\n가 : {}명".format(soo, woo, mi, yang, ga))

numbers = [[10, 20, 30], [40, 50, 60]]
for numberz in numbers:
  print(numberz)
for numberz in numbers:
  for number in numberz:
    print(number, end=' ')
  print()

data = [[10, 20], [30, 40], [50, 60], [70, 80]]
for i in range(4):
  for j in range(2):
    print("data[%d][%d] = %d"%(i, j, data[i][j]))

strings = [["원두커피", "라떼", "콜라"], ["우동", "국수", "피자", "파스타"]]

for i in range(strings.len()):
  for j in range(strings[i].len()):
    print(strings[i][j], end=' ')
  print()