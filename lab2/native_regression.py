from matrix import *
import matplotlib.pyplot as plt
import sys

data = loadtxt(sys.argv[1])

X = [row[0] for row in data]
Y = [row[1] for row in data]

Xp = powers(X, 0, 1)
Yp = powers(Y, 1, 1)
Xpt = transpose(Xp)

[[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))


chirps = [b + m * x for x in X]

plt.plot(X, Y, 'ro')
plt.plot(X, chirps)
plt.xlabel("Temperature")
plt.ylabel("Chirps per minute")
plt.title("Linear Regression")
plt.show()