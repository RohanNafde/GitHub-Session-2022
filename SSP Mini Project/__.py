import main
import numpy as np
from matplotlib import pyplot as plt

x = np.empty(1001, dtype=float)

for i in range(0, 1001):
    x[i] = 0.01 * i

plt.plot(x, main.v_w_m[0])
plt.plot(x, main.v_w_m[1])
plt.plot(x, main.v_w_m[2])
plt.show()

# Quit the previous plot to see the below plot

plt.plot(x, main.v_q_m[0])
plt.plot(x, main.v_q_m[1])
plt.plot(x, main.v_q_m[2])
plt.plot(x, main.v_q_m[3])
plt.show()
