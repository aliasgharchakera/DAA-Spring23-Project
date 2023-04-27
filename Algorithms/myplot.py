import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import knapsack_dp
import knapsack_EA
import knapsack_greedy

n_list, dp_time, c_list = knapsack_dp.main()
n_list, ea_time, c_list = knapsack_EA.main()
n_list, greedy_time, c_list = knapsack_greedy.main()

# w_list, v_list, dp_time = knapsack_dp.main()
# w_list, v_list, ea_time = knapsack_EA.main()
# w_list, v_list, greedy_time = knapsack_greedy.main()

# x = np.random.rand(20)
# y = np.random.rand(20)
# z = x*y

plt.plot(n_list, dp_time, color="red")
plt.plot(n_list, ea_time, color="blue")
plt.show(n_list, greedy_time, color="green")
plt.show()
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(w_list, v_list, greedy_time,
#            linewidths=1, alpha=.7,
#            edgecolor='k',
#            s = 200,
#            c=greedy_time)
# ax.set_xlabel('Avg wi')
# ax.set_ylabel('Avg vi')
# ax.set_zlabel('Time(s)')
# plt.show()