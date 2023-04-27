''' This file contains code for analysis(plotting) of the 3 algorithms used w.r.t their run times. The 3 algorithms used are:
    1 - Dynamic Programming 
    3 - Evolutionary Algorithm
    2 - Greedy Algorithm '''

import matplotlib.pyplot as plt

# For Dynamic Programming:
# import knapsack_dp
from knapsack_dp import dpplot

dp_data = []
dpplot(dp_data)

# For EA:
# import knapsack_EA
from knapsack_EA import eaplot

EA_data = []
eaplot(EA_data)

# For Greedy:
# import knapsack_greedy
from knapsack_greedy import greedyplot

greedy_data = []
greedyplot(greedy_data)

print(dp_data)

# Main plot
def mainplot():
    plt.plot(dp_data[0], dp_data[1], color='blue', label='DP')
    plt.plot(EA_data[0], EA_data[1], color='red', label='EA')
    plt.plot(greedy_data[0], greedy_data[1], color='green', label='Greedy')
    # plt.loglog(x_values, y_values)
    # plt.xlabel('n')
    # plt.ylabel('Time (seconds)')
    # plt.grid()
    plt.legend()
    plt.title('Knapsack')
    plt.show()

mainplot()
