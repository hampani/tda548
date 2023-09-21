import matplotlib.pyplot as plt
from numpy import *
import sys


def powers(row, start, end):
    new_row = []
    for number in row:
        rows = []
        for element in range(start, end + 1):
            rows.append(number ** element)
        new_row.append(rows)
    return array(new_row)


def poly(a, X):
    result = []
    for x in X:
        Y2 = 0
        for idx, coeff in enumerate(a):
            Y2 += coeff*(x**idx)
        result.append(Y2)
    return result


data = loadtxt(sys.argv[1])
n = int(sys.argv[2])

X = data[:, 0]
Y = data[:, 1]


Xp = powers(X, 0, n)
Yp = powers(Y, 1, 1)
Xpt = transpose(Xp)

a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
a = a[:, 0]

X2 = linspace((X[0]), (X[-1]), int((X[-1]-X[0])/0.2)).tolist()


Y2 = poly(a, X2)

plt.plot(X, Y, 'ro')
plt.plot(X2, Y2)
plt.xlabel("Temperature")
plt.ylabel("Chirps per minute")
plt.title("Polynomial Regression")
plt.show()
