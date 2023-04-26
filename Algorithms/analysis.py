''' This file contains code for analysis(plotting) of the 3 algorithms used w.r.t their run times. The 3 algorithms used are:
    1 - Dynamic Programming 
    3 - Evolutionary Algorithm
    2 - Greedy Algorithm '''

import matplotlib.pyplot as plt

# For Dynamic Programming:
from knapsack_dp import *

dp_data = []
def dp():
    knapsack_dp.main(dp_data)
    for data in dp_data :
        plt.plot(data[0], data[1], color='blue', label="")
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Knapsack - DP')
    plt.show()

dp()

# For EA:
from knapsack_EA import *
EA_data = []

# For Greedy:
from knapsack_greedy import *
greedy_data = []


# Main plot
