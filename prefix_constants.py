import numpy as np

m_MOI = np.array([[0.3, 0.2, 1.0],
                  [0.8, 0.5, 0.9],
                  [0.6, 0.7, 1.1]])

v_W = np.array([0.2, 0.5, 0.8])

v_M = np.array([0.3, 0.4, 0.5])

v_Q = np.array([0, 0, 0, 1])

H = 0.01
T = 10
N = int(H / T)
