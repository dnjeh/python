import csv
import matplotlib.pyplot as plt

f=open("2022_12_08_T11.csv", 'r')

rows=csv.reader(f)
next(rows)
x=[]
y=[]
z=[]
xx=[]
t=[]
tt=[]

for n, row in enumerate(rows):
    if n<2:
        continue
    x.append(int(row[0]))
    y.append(float(row[9]))
    z.append(float(row[10]))
    xx.append(float(row[11]))
    t.append(float(row[15]))
    tt.append(float(row[20]))

#plt.plot(x, y, label="y movement")
#plt.plot(z, label="z movement")
#plt.plot(xx, label="xx movement")
plt.plot(x, t, label="spindle load")
plt.plot(tt, label="act load")

plt.xlabel("Number of times", color="red")
plt.ylabel("Loads", color="blue")
plt.legend()

plt.title("Load")

plt.show()
f.close()
