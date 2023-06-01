strings = [["원두커피", "라떼", "콜라"], ["우동", "국수", "피자", "파스타"]]
for i in range(len(strings)):
  for j in range(len(strings[i])):
    print(strings[i][j], end=' ')
  print()

data = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
print(data)
for i in data:
  print(i[0])

score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]
total = 0
totalsub = 0
for i in score:
  cnt = 0
  for j in i:
    cnt += j
    total += j
    totalsub += 1
  print("총점 {} 평균 {}".format(cnt, cnt/len(i)))
print("전체평균 {}".format(total/totalsub))

seats = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,1,0,0,0,1,0,1,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [1,0,1,0,0,0,0,0,0,1]
]
for i in range(len(seats)):
  for j in range(len(seats[i])):
    if seats[i][j] == 0:
      print("%3s" % '□', end='')
    else:
      print("%3s" % '■', end='')
  print()
print("\n※ 예약 가능 : ■, 예약 불가 : □")

scores= [[96, 84, 80], [96, 86, 76], [76, 95, 83], [89, 96, 69], [83, 86, 79], [85, 90, 83]]
i=0
while i < 6:
  j=0
  sum=0
  while j < 3:
    sum+=scores[i][j]
    j+=1
  print("{}번째 학생의 합계 : {}, 평균 : {}".format(i+1, sum, sum/len(scores[i])))
  i+=1

scores= [[96, 84, 80], [96, 86, 76], [76, 95, 83], [89, 96, 69], [83, 86, 79], [85, 90, 83]]
h=0
for i in scores:
  sum=0
  for j in i:
    sum+=j
  print("{}번째 학생의 합계 : {}, 평균 : {}".format(h+1, sum, sum/len(i)))
  h+=1

even1 = [2 * n for n in range(1, 51)]
even2 = [n for n in range(1, 101) if n%2==0]
print(even1)
print(even2)

li = []
for n in range(1, 10):
  if n%3==0:
    li.append(n*n)
print(li)

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)

v = [17, 92, 18, 33, 58, 7, 33, 42]

max=v[0]
for i in range(len(v)):
  if max<v[i]:
    max=v[i]
print("최대값 = {}".format(max))

for i in [1, 2, 3]:
  for j in ['a', 'b', 'c']:
    print(j*i, end=' ')

list_a = ['I', "study", "python", "language", "!"]
for i in list_a:
  if(len(i)>=3):
    print(i)