import numpy as np
import prefix_constants
from numpy.linalg import inv

# n is time steps

n = prefix_constants.N

v_w_m = np.empty([3, 1001], dtype=float)

v_w_m[0][0] = prefix_constants.v_W[0]
v_w_m[1][0] = prefix_constants.v_W[1]
v_w_m[2][0] = prefix_constants.v_W[2]


def w_dot(w):
    return inv(prefix_constants.m_MOI).dot(prefix_constants.v_M - np.cross(w, prefix_constants.m_MOI.dot(w)))


def rk4_w(y):
    h = prefix_constants.H

    k1_st = w_dot(y)
    k2_st = w_dot(y + h / 2 * k1_st)
    k3_st = w_dot(y + h / 2 * k2_st)
    k4_st = w_dot(y + h * k3_st)

    return y + h / 6 * (k1_st + 2 * k2_st + 2 * k3_st + k4_st)


for i in range(0, 1000):
    w_st = np.array([v_w_m[0][i], v_w_m[1][i], v_w_m[2][i]])

    w_next_st = rk4_w(w_st)
    v_w_m[0][i + 1] = w_next_st[0]
    v_w_m[1][i + 1] = w_next_st[1]
    v_w_m[2][i + 1] = w_next_st[2]
