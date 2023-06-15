
a = "a:b:c:d"
print(a.split(':'))

print('.'.join('abcd'))
print('::'.join(["나는", "밥을", "먹는다"]))

a = "10 20 30 40 50"
print(a.split())
b = "나는 서울로봇고 2학년이야."
print(b.split())

BTS = "정국, 진, 뷔, 슈가, 지민, RM, 제이홉"
BTS_member = BTS.split(", ")
print("방탄 멤버:", BTS_member)

for mem in BTS_member:
  print(mem, "사랑해")

file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]

for file in file_names:
  arr = file.split('.')
  print(file, " => 파일명:", arr[0], ", 확장자:.", arr[1], sep='')

sentence = input("문자열 입력: ")
a = sentence.split(' ')
for i in a:
  print(i[0], end='')

print(','.join("abcd"))
print("::".join("12345"))

s = "python programming"

print("문자열 s의 길이 =", len(s))
print()
print("문자열 s에서 o의 인덱스 =", s.find('o'))
print("문자열 없는 인덱스를 검색=", s.find('z'))
print("o를 뒤에서부터 검색한 인덱스 =", s.rfind('o'))
print()
print("문자열 s에서 r의 인덱스 =", s.find('r'))
print("문자열 s에서 n의 개수 =", s.count('n'))
print()
print("문자열 s에서 gram의 인덱스 =", s.find('gram'))
print("문자열 s에서 gram의 개수 =", s.count('gram'))
print("문자열 s에서 gram의 개수 =", s.count('gram'))

name = "박보검"
if name.startswith("박"):
  print("박씨입니다.")
elif name.startswith("김"):
  print("박씨입니다.")

file = "HelloPython.jpg"
if file.endswith(".jpg"):
  print("그림 파일입니다.")

domain = "http://www.soen.kr"
if domain.endswith(".kr"):
  print("한국 도메인입니다.")

s = "python programming"
print('a' in s)
print('z' in s)
print("pro" in s)
print("x" not in s)

s = input("영어 문장을 입력하세요 :")
i = 0
count = 0
print("모음 : ", end='')
while i<len(s):
  if s[i]=='a' or s[i]=='o' or s[i]=='i' or s[i]=='e' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
    print(s[i], end=' ')
    count+=1
  i+=1
print("\n모음의 개수 :", count)

height = input("키를 입력하세요:")
if height.isnumeric():
  print("키는", height, "입니다.")
else:
  print("숫자로 입력하세요.")

data = input("문자열 입력:")

for i in data:
  if i.islower():
    print('X', end='')
  else:
    print('O', end='')

s = "good morning. MyLove Kim."

print("문자열:", s)
print("대문자로 번경:", s.upper())
print("소문자로 번경:", s.lower())

print("대소문자 반대로 번경:", s.swapcase())
print("첫 글자만 대문자로 번경:", s.capitalize())
print("모든 글자의 첫 글자를 대문자로 번경:", s.title())

python = input("파이썬의 영문 철자를 입력하시오:")
if python.lower() == "python":
  print("맞췄습니다.")

char = input("영문 대문자 또는 소문자 하나를 입력하세요 : ")
char2 = char.upper()
if char2 == 'A' or char2 == 'E' or char2 == 'I' or char2 == 'O' or char2 == 'U' :
  print("%s -> 모음" % char)
else :
  print("%s -> 자음" % char)

f = open("노래가사.txt", 'r')
data = f.read()

data = data.count("rollin")

phone_list1 = ["010-3654-2637", "010-3984-5377", "010-3554-0973"]
print(phone_list1)

phone_list2 = []
for phone in phone_list1:
  x = phone.replace('-', '')
  phone_list2.append(x)
print(phone_list2)

sentences = ["Love me, love my dog.", "Np news is good news", "Blood is thicker than water"]

for s in sentences:
  x = s.replace(' ', '_')
  print(x)

s = "  angel   "
print(s+"님")
print(s.lstrip()+"님")
print(s.rstrip()+"님")
print(s.strip()+"님")

phone = input("하이픈(-)을 뺀 11자리의 휴대폰 번호를 입력하세요: ")
number = ""
for i in range(11):
  if i==2:
    number = number + phone[i] + '-'
  elif i==6:
    number = number + phone[i] + '-'
  else:
    number = number + phone[i]
print(number)

s = "a:b:c:d"
s = s.replace(':', '#')
print(s)

s = "아침에 일어나서 콜라를 한 잔 마시고 밥 먹고 콜라 마시고 자기 전에도 콜라를 마신다."
s = s.replace("콜라", "우유")
print(s)

s = "python"
s[2] = 'K'

a = "Tom Dick Harry"
a = a.split()
for i in range(len(a)):
  a[i]=sorted(a[i])
  a[i]=''.join(a[i])
print(", ".join(a))

word = input("영어 단어를 입력하세요: ")
ubbi = ""
for i in word:
  if i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U':
    ubbi+="ub"+i
  else:
    ubbi+=i
print(ubbi)

word = input("단어를 입력하세요: ")
count = 0

for i in word:
  if i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U':
    count+=1
if count==1:
  print(word[1:]+word[0]+"ay")
else:
  print(word+"way")

word = input("단어를 입력하세요: ")
count = 0
if word[0].upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U':
  print(word+"way")
else:
  print(word[1:]+word[0]+"ay")

sentence = input("문자열 입력: ")
new = ""
now = ''
count = 0

for i in sentence:
  if now == i:
    count+=1
  else:
    new+=(now+str(count) if count>0 else '')
    now=i
    count=1
new+=(now+str(count))
print(new)

"""# 수행평가 문제들 전용"""

animals = ["토끼", "거북이", "사자", "호랑이"]
for i in range(len(animals)):
  print(animals[i])
for i in animals:
  print(i)

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

score = [88,95,70,100,99]
score.remove(99)
print("99삭제 후 :", score)
score.sort()
print("리스트 정렬 후:", score)
score.reverse()
print("거꾸로 정렬:", score)
score.clear()
print("리스트 삭제:", score)

list1 = ['a', 'bb', 'c', 'd', 'aaa', 'c', 'ddd', 'aaa',
'b', 'cc', 'd', 'aaa']
length = list1.count('aaa')
print(length)

mylist = ['사과', '바나나', '파인애플']
mylist.append('키위')
mylist.append('배')
for a in mylist:
  print(a)

emails = [["kim", "naver.com"], ["hwang","hanmail.net"], ["lee", "korea.com"], ["choi","gmail.com"]]
email_new = []
for email in emails:
  email_new.append(email[0] + "@" + email[1])
print(email_new)

score = [1, 3, 5, 7, 9, 11, 13]
cnt = 0
for num in score :
  if num < 10:
    cnt+=1
    print(num , end = ' ')
print('\n10보다 작은 수의 개수 :', cnt)

score = []
sum=0
for i in range(5):
  score.append(int(input("성적입력: ")))
  sum+=score[i]
print(score)
print("총점은", sum, "이고, 평균은", sum/len(score), "입니다.")

data = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
print(data)
for i in data:
  print(i[0])

score = [
  [88,76,92,98],
  [65,70,58,82],
  [82,80,78,88],
]
total = 0 #모든 학생 점수 합
totalsub = 0 #모든 학생 과목 수

for sco in score:
  sum=0
  for s in sco:
    sum+=s
    total+=s
  print("총점", sum, "평균", sum/len(sco))
  totalsub+=len(sco)
print("전체평균", total/totalsub)

questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answers = ['a', 'u', 't','p']
count = 0
for i in range(4) :
  q = '%s 에서 밑줄(_) 안에 들어갈 알파벳은? '%questions[i]
  ans = input(q)
  if ans==answers[i]:
    print('정답입니다!')
    count+=1
  else :
    print('틀렸습니다!')
print("당신의 점수는 %d/4 입니다."%count)

scores = [[96, 84, 80], [96, 86, 76], [76, 95, 83],
[89, 96, 69], [83, 86, 79], [85, 90, 83]]
for score in scores:
  sum=0
  for sco in score:
    sum+=sco
  print(scores.index(score)+1, "번째 학생의 합계 :", sum, ", 평균 : {:.2f}".format(sum/len(score)))

li = []
for n in range(1, 10):
  if n%3 == 0:
    li.append(n*n)
print(li)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)

for i in [1,2,3]:
  for a in ['a','b','c']:
    print(a*i, end=' ')

sentence = input("문장을 입력해 주세요 : ")

i=1
while i<=len(sentence):
  if(sentence[-i]==' '):
    print('-', end='')
  else:
    print(sentence[-i], end='')
  i+=1

jumin = "901231-1914983"
year = jumin[0:2]
if int(jumin[jumin.index('-')+1])%2 == 0:
  gender = "여자"
else:
  gender = "남자"
print("{}년생 {}입니다.".format(year, gender))

BTS = "정국, 진, 뷔, 슈가, 지민, RM, 제이홉"
BTS_member = BTS.split(", ")
print("방탄 멤버:", BTS_member)

for mem in BTS_member:
  print(mem, "사랑해")

file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]

for file in file_names:
  arr = file.split('.')
  print(file, " => 파일명:", arr[0], ", 확장자:.", arr[1], sep='')

sentence = input("문자열 입력: ")
a = sentence.split(' ')
for i in a:
  print(i[0], end='')

print(','.join("abcd"))
print("::".join("12345"))

s = "python programming"
print('a' in s)
print('z' in s)
print("pro" in s)
print("x" not in s)

s = input("영어 문장을 입력하세요 :")
i = 0
count = 0
print("모음 : ", end='')
while i<len(s):
  if s[i]=='a' or s[i]=='o' or s[i]=='i' or s[i]=='e' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
    print(s[i], end=' ')
    count+=1
  i+=1
print("\n모음의 개수 :", count)

height = input("키를 입력하세요:")
if height.isnumeric():
  print("키는", height, "입니다.")
else:
  print("숫자로 입력하세요.")

data = input("문자열 입력:")

for i in data:
  if i.islower():
    print('X', end='')
  else:
    print('O', end='')

s = "good morning. MyLove Kim."

print("문자열:", s)
print("대문자로 번경:", s.upper())
print("소문자로 번경:", s.lower())

char = input("영문 대문자 또는 소문자 하나를 입력하세요 : ")
char2 = char.upper()
if char2 == 'A' or char2 == 'E' or char2 == 'I' or char2 == 'O' or char2 == 'U' :
  print("%s -> 모음" % char)
else :
  print("%s -> 자음" % char)

phone_list1 = ["010-3654-2637", "010-3984-5377", "010-3554-0973"]
print(phone_list1)

phone_list2 = []
for phone in phone_list1:
  x = phone.replace('-', '')
  phone_list2.append(x)
print(phone_list2)

s = "a:b:c:d"
s = s.replace(':', '#')
print(s)

phone = input("하이픈(-)을 뺀 11자리의 휴대폰 번호를 입력하세요: ")
number = ""
for i in range(11):
  if i==2:
    number = number + phone[i] + '-'
  elif i==6:
    number = number + phone[i] + '-'
  else:
    number = number + phone[i]
print(number)

a = "Tom Dick Harry"
a = a.split()
for i in range(len(a)):
  a[i]=sorted(a[i])
  a[i]=''.join(a[i])
print(", ".join(a))

word = input("단어를 입력하세요: ")
count = 0

for i in word:
  if i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U':
    count+=1
if count==1:
  print(word[1:]+word[0]+"ay")
else:
  print(word+"way")

sentence = input("문자열 입력: ")
new = ""
now = ''
count = 0

for i in sentence:
  if now == i:
    count+=1
  else:
    new+=(now+str(count) if count>0 else '')
    now=i
    count=1
new+=(now+str(count))
print(new)

yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])

sentence = input("문자열 입력:")
for i in range(len(sentence)):
  if sentence[i] == 't':
    print(i+1, end=' ')

number = input("하이픈(-)을 포함한 휴대번호를 입력하세요: ")
for i in number:
  if i!='-':
    print(i, end='')
