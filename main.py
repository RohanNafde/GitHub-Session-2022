import numpy as np
import prefix_constants
from numpy.linalg import inv
from matplotlib import pyplot as plt

# n is time steps

n = prefix_constants.N

v_w_m = np.empty([3, 11], dtype=float)
q = np.empty([4, 11], dtype=float)

v_w_m[0][0] = 0.2
v_w_m[1][0] = 0.5
v_w_m[2][0] = 0.8

q[0][0] = 1
q[1][0] = 0
q[2][0] = 0
q[3][0] = 0


def f(w):
    return inv(prefix_constants.m_MOI).dot(prefix_constants.v_M - np.cross(w, prefix_constants.m_MOI.dot(w)))


def rk4(w):
    h = prefix_constants.H
    k1_st = f(w)
    k2_st = f(w + h / 2 * k1_st)
    k3_st = f(w + h / 2 * k2_st)
    k4_st = f(w + h * k3_st)
    return w + h / 6 * (k1_st + 2 * k2_st + 2 * k3_st + k4_st)


for i in range(0, 10):
    w_st = np.array([v_w_m[0][i], v_w_m[1][i], v_w_m[2][i]])
    wnext_st = rk4(w_st)
    v_w_m[0][i + 1] = wnext_st[0]
    v_w_m[1][i + 1] = wnext_st[1]
    v_w_m[2][i + 1] = wnext_st[2]

x = np.arange(0, 11)
plt.plot(x, v_w_m[0])
plt.plot(x, v_w_m[1])
plt.plot(x, v_w_m[2])
plt.show()
