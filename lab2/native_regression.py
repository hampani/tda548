from matrix import *
import matplotlib.pyplot as plt
import numpy as np
import sys

data = np.loadtxt(sys.argv[1])

X = data[:, 0]
Y = data[:, 1]

Xp = powers(X, 0, 1)
Yp = powers(Y, 1, 1)
Xpt = transpose(Xp)

[[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))


chirps = b + m * X

plt.plot(X, Y, 'ro')
plt.plot(X, chirps)
plt.xlabel("Temperature")
plt.ylabel("Chirps per minute")
plt.title("Linear Regression")
plt.show()
