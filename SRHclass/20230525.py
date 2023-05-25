score = [88, 95, 70, 100, 99]
score[0]=10
score[1]=20
score[2]=30
score[-2]=40
score[-1]=50
print(score)

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

file = "20210505-104830.jpg";
print("촬영 날짜: "+file[4:6]+"월"+file[6:8]+"일")
print("촬영 시간: "+file[9:11]+"시"+file[11:13]+"분")
print("확장자:"+file[-3:])