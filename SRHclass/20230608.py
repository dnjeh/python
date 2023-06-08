score = [ 
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]
total=0
totalsub=0

for student in range(len(score)):
  sum=0
  for subject in range(len(score[student])):
    sum+=score[student][subject]
  number = len(score[student])
  print("총점: {} 평균: {}".format(sum, sum/number))
  total+=sum
  totalsub+=number
print("전체평균:", total/totalsub)


s = "python"
print(s[0])
print(s[-1])


s = "python"
print(s[10])


S1=input("첫번째 문자열:")
S2=input("두번째 문자열:")
S3=input("세번째 문자열:")
if S1[-1]==S2[0] and S2[-1]==S3[0] and S3[-1]==S1[0]:
  print("good")
else:
  print("bad")


s = "python"
for c in s:
  print(c, end = ',')
print()


s="python"
for i in range(len(s)):
  print(s[i], end=',')


number = input("하이픈(-)을 포함한 전화번호를 입력하세요: ")

for num in number:
  if num != '-':
    print(num, end='')


s="python"
print(len(s))
n = "여섯글자이다"
print(len(n))


sentence = input("문자열 입력:")

for i in range(len(sentence)):
  if sentence[i] == 't':
    print(i+1, end=' ')


sentence = input("문장을 입력해 주세요 : ")

i=(len(sentence))-1
while i>=0:
  print(sentence[i] if sentence[i]!=' ' else '-', end='')
  i-=1


data = input("문자열 입력:")

for i in range(len(data)-1):
  print(data[i], data[i+1], sep='')


s = "python"
print(s[2:5])
print(s[-3:])
print(s[:4])
print(s[2:4])
print(s[-2:])


s = "차종: 코란도C, 제조사:쌍용, 배기량: 1998"
print(s[14:16])


file = "20210505-104830.jpg";
print("촬영 날짜: "+file[4:6]+"월"+file[6:8]+"일")
print("촬영 시간: "+file[9:11]+"시"+file[11:13]+"분")
print("확장자:"+file[-3:])


yoil = "월화수목금토일"
print(yoil[0::2])
print(yoil[-1::-1])


jumin = "901231-1914983"
year = jumin[0:2]
if int(jumin[7:8])%2==0:
  gender = "여자"
else:
  gender = "남자"
print("{}년생 {}입니다.".format(year, gender))


a = "10 20 30 40 50"
print(a.split())
b = "나는 서울로봇고 2학년이야."
print(b.split())


a = "a:b:c:d"
print(a.split(':'))

print('.'.join("abcd"))
print("::".join(["1", "2", "3"]))