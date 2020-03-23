import pandas
import numpy as np
import matplotlib.pyplot as plt
data = pandas.read_csv("student-mat.csv", sep=';')
data = data[["G1","G2","G3","absences","studytime"]]
X = np.array(data["G1"])
y = np.array(data["G2"])
z = np.array(data["G3"])
x = np.array(data["G1"], data["G2"])

for n, i in enumerate(z):
    if z[n] > 10:
        z[n] = 1
    else:
        z[n] = 0

X1 = np.array(data[["G1", "G2"]])
red = [X1[np.argwhere(z == 0)]]
blue = [X1[np.argwhere(z == 1)]]
print('len(red) =', len(red))
for m,s in enumerate(red[0]):
    print(m)
    if m == 393:
        break
    plt.scatter(s[0][0], s[0][1], s=25, color="red", edgecolor='k')
for m,s in enumerate(blue):
    if m == 393:
        break
    plt.scatter([s[0][0][m]], [s[0][0][m+1]], s=25, edgecolors="k", color='blue')
plt.xlabel("G1")
plt.ylabel("G2")



plt.show()
