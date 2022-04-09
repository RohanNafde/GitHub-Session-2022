import numpy as np

m_MOI = np.array([[0.3, 0.2, 1.0],
                  [0.8, 0.5, 0.9],
                  [0.6, 0.7, 1.1]])

v_M = np.array([0, 0, 0])

H = 0.01
T = 10
N = T / H
