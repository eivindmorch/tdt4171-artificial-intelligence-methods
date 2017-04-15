import numpy as np
import random
import matplotlib.pyplot as plt


r = np.arange(-6, 6.0001, 0.05)
w1_matrix, w2_matrix = np.meshgrid(r, r)


def delta(w, x):
    return 1 / (1 + np.exp(- np.inner(w, x)))


# def delta(x):
#     return 1 / (1 + np.exp(-x))
def L_simple(w):
    p1 = (delta(w, [1, 0]) - 1) ** 2
    p2 = (delta(w, [0, 1])) ** 2
    p3 = (delta(w, [1, 1]) - 1) ** 2
    return p1 + p2 + p3


# def L_simple(w):
#     p1 = (delta(w[0]) - 1) ** 2
#     p2 = (delta(w[1])) ** 2
#     p3 = (delta(w[0]+w[1]) - 1) ** 2
#     return p1 + p2 + p3
def updateWeights(w):
    w[0] += - learning_rate * (L_simple_deriv(w, 0))
    w[1] += - learning_rate * (L_simple_deriv(w, 1))


def L_simple_deriv(w, i):
    a = (delta(w, [1, 0]) - 1) * (delta(w, [1, 0])) * (1 - delta(w, [1, 0])) * [1, 0][i]
    b = (delta(w, [0, 1]))     * (delta(w, [0, 1])) * (1 - delta(w, [0, 1])) * [0, 1][i]
    c = (delta(w, [1, 1]) - 1) * (delta(w, [1, 1])) * (1 - delta(w, [1, 1])) * [1, 1][i]
    return a + b + c


values = [[None for i in range(len(r))] for i in range(len(r))]
for i in range(len(r)):
    for j in range(len(r)):
        w = [w1_matrix[i][j], w2_matrix[i][j]]
        values[i][j] = L_simple(w)


learning_rate = 0.1
w = [r[random.randint(0, r.size - 1)], r[random.randint(0, r.size - 1)]]
c = 1
w_storage = []
for i in range(0, 100000):
    # print(L_simple(w))
    w_storage.append(w)
    updateWeights(w)
    if i % 1000 == 0:
        print(L_simple(w))

print(w_storage)

# fig = plt.figure()
# plt.plot()
# plt.pcolormesh(w1_matrix, w2_matrix, values, cmap='RdBu')
# plt.colorbar()
# plt.show()
