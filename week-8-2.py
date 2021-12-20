import numpy as np
np.random.seed(1990)

def sum_square_error(y, y_hat):
    err = y - y_hat
    return np.sum(np.power(err, 2))

b_1_true = 3
b_0_true = 10

def f_1(x):
    n = len(x)
    y = b_1_true*x + b_0_true + np.random.normal(0, 5, n)
    return y

x = np.arange(0, 20)
y = f_1(x)


b_0_arr = np.arange(0, 20, step=0.1)
b_1_arr = np.arange(-10, 10, step=0.1)

sse = []
b_0_all = []
b_1_all = []

for b_0_i in b_0_arr:
  for b_1_j in b_1_arr:
    b_0_all.append(b_0_i)
    b_1_all.append(b_1_j)
    y_hat = b_1_j*x + b_0_i
    sse.append(sum_square_error(y, y_hat))

sse = np.array(sse)
sse = sse.reshape(len(b_0_arr), len(b_1_arr))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(
        np.array(b_0_all).reshape(len(b_0_arr), len(b_1_arr)),
        np.array(b_1_all).reshape(len(b_0_arr), len(b_1_arr)),
        sse
    )
ax.set_xlabel('b_0')
ax.set_ylabel('b_1')
ax.set_zlabel('Error')

plt.show()
