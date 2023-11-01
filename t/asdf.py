import csv
import matplotlib.pyplot as plt

f=open("2022_12_08_T11.csv", 'r')

rows=csv.reader(f)
next(rows)
x=[]
y=[]
z=[]
xx=[]

for n, row in enumerate(rows):
    if n<2:
        continue
    x.append(int(row[0]))
    y.append(float(row[9]))
    z.append(float(row[10]))
    xx.append(float(row[11]))

plt.plot(x, y, label="y movement")
plt.plot(z, label="z movement")
plt.plot(xx, label="xx movement")

plt.xlabel("Number of times", color="red")
plt.ylabel("movement", color="blue")
plt.legend()

plt.title("Movement of x,y,z")

plt.show()
f.close()