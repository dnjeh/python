import random
import csv
f = open("name.csv")
f2 = open("present.csv")
name = csv.reader(f)
present = csv.reader(f2)
header=next(name)
header=next(present)
name = list(name)
present = list(present)
f.close()
f2.close()
print(f"축하합니다! {}님이 {}을/를 획득하셨습니다!".format(random.choice(name), random.choice(present)))
