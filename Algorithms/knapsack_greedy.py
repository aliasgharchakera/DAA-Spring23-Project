# The 0/1 knapsack problem is a classic optimization problem where we have a set of items, each with its own weight and value, and a knapsack with a certain weight capacity. 
# The goal is to select a subset of the items to maximize the total value that can be carried in the knapsack without exceeding its weight capacity. A greedy algorithm for the 0/1 knapsack problem can be formulated as follows:

# Sort the items in decreasing order of their value-to-weight ratios (i.e., value divided by weight).
# Initialize the total value and weight to zero and the set of selected items to empty.
# For each item in the sorted list:
# a. If adding the item to the selected items set does not exceed the knapsack weight capacity, add it and update the total value and weight.
# b. If adding the item exceeds the knapsack weight capacity, skip it and move on to the next item.
# Return the set of selected items and the total value.
# This greedy algorithm works by selecting the items with the highest value-to-weight ratios first, which gives us the maximum possible value per unit weight. 
# By continuing to add items in this manner until the knapsack capacity is reached, we can achieve a locally optimal solution, but not necessarily the globally 
# optimal one. However, this algorithm can be a good approximation for large problem sizes where more efficient dynamic programming solutions may not be feasible.

# The time complexity of the greedy algorithm for the 0/1 knapsack problem depends on the sorting algorithm used to sort the items by value-to-weight ratio.
# Assuming a comparison-based sorting algorithm is used, such as quicksort or mergesort, the time complexity of sorting is O(n log n), where n is the number of items.
# After sorting the items, the algorithm examines each item in the sorted list once and either adds it to the selected set or skips it, taking constant time for each item. Therefore, the time complexity of the algorithm's main loop is O(n).
# Combining these two steps, the overall time complexity of the greedy algorithm for the 0/1 knapsack problem is O(n log n) + O(n) = O(n log n).
# Note that this is the worst-case time complexity of the algorithm, assuming no special structure in the item weights or values. 
# In practice, the actual running time of the algorithm may be much faster, especially if the items are already sorted or the input size is small.

def knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    selected_items = []

    for value, weight in items:
        if capacity >= weight:  # If item fits in knapsack
            total_value += value
            selected_items.append((value, weight))
            capacity -= weight

    return total_value


# Example usage
# items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # List of items with (weight, value) pairs
# capacity = 8  # Knapsack weight capacity

# total_value, selected_items = knapsack(items, capacity)
# print("Total value:", total_value)
# print("Selected items:", selected_items)


import os
from sys import path
path.append("../Dataset/")
import time
import statistics
from contextlib import contextmanager
import matplotlib.pyplot as plt

@contextmanager
def timer(label: str, timelst):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        # print(f"{label}: {end - start:.3f} seconds")
        timelst.append(end-start)

# main()
def main():
    # categories = ["very_large_n", "very_large_wmax", "very_large_n_and_wmax",  "very_large_valued_V", "very_large_valued_W", "very_large_valued_V_and_W"]
    categories = ["very_large_n"]
    # categories = ["very_large_valued_V_and_W"]
    instances = 100
    iterations = 3
    avg_score = list(); avg_time = list()
    n_lst = list(); c_lst = list()
    v_lst = list(); w_lst = list()
    for c in categories:
        for i in range(instances):
            score = list()
            timelst = list()
            
            num = "0"*(4-len(str(i)))
            location = f"../Dataset/{c}_group/instance_{num}{i}.txt"
            items = list(); W = list(); V = list()
            with open(location) as f:
                lines = f.readlines()
                num, capacity = lines[0].split()
                num, capacity = int(num), int(capacity)
                for i in lines[1::]:
                    value, weight = i.split()
                    items.append((int(value), int(weight)))
                    W.append(int(weight)); V.append(int(value))
                    
            for i in range(iterations):
                with timer("func", timelst):
                    max = knapsack(items, capacity)
                score.append(max)
            w_lst.append(statistics.mean(W))
            v_lst.append(statistics.mean(V))
            n_lst.append(num)
            c_lst.append(capacity)
            avg_score.append(statistics.mean(score))
            avg_time.append(statistics.mean(timelst))
            n_t = list(zip(n_lst, avg_time, c_lst))
            # n_t = list(zip(w_lst, avg_time, v_lst))
            n_t.sort(key=lambda x: x[0])
            # n_t is a list of tuples of (n, time), I want two separate lists of n and time
            n_list, time_list, c_list = zip(*n_t)
            # w_list, time_list, v_list = zip(*n_t)
    # with open('analysis3.csv', 'w') as f:
    #     f.write("score, time\n")
    #     for i in range(instances*len(categories)):
    #         if i % instances == 0:
    #             f.write(f"{categories[i//instances]}\n")
    #         f.write(f"{avg_score[i]}, {avg_time[i]}, {n_lst[i]}\n")
    
    # plt.plot(n_list, time_list, label="max")
    # plt.show()
    # plotting_instances.append((n_list, time_list))
    # return plotting_instances
    return n_list, time_list, c_list
    # return w_list, v_list, time_list


if "__name__" == "__main__":
    main()

def wmax(plotting_instances):
    categories = ["very_large_wmax"]
    instances = 100
    iterations = 1
    avg_score = list(); avg_time = list()
    n_lst = list(); c_lst = list()
    for c in categories:
        for i in range(instances):
            score = list()
            timelst = list()
            
            num = "0"*(4-len(str(i)))
            location = f"../Dataset/{c}_group/instance_{num}{i}.txt"
            items = list(); W = list(); V = list()
            with open(location) as f:
                lines = f.readlines()
                num, capacity = lines[0].split()
                num, capacity = int(num), int(capacity)
                for i in lines[1::]:
                    value, weight = i.split()
                    items.append((int(value), int(weight)))
                    W.append(int(weight)); V.append(int(value))
                    
            for i in range(iterations):
                with timer("func", timelst):
                    max = knapsack(items, capacity)
                score.append(max)
            n_lst.append(num)
            c_lst.append(capacity)
            avg_score.append(statistics.mean(score))
            avg_time.append(statistics.mean(timelst))
            c_t = list(zip(c_lst, avg_time))
            c_t.sort(key=lambda x: x[0])
            # n_t is a list of tuples of (n, time), I want two separate lists of n and time
            c_list, time_list = zip(*c_t)
    with open('analysis2.csv', 'w') as f:
        f.write("score, time\n")
        for i in range(instances*len(categories)):
            if i % instances == 0:
                f.write(f"{categories[i//instances]}\n")
            f.write(f"{avg_score[i]}, {avg_time[i]}\n")
    
    plotting_instances.append((c_list, time_list))
    return plotting_instances


def greedyplot(plotting_instances = []):
    # plotting_instances= []
    plotting_instances.append(main(plotting_instances))
    # wmax(plotting_instances)
    # print(plotting_instances)
    for data in plotting_instances:
        plt.plot(data[0], data[1], color='blue')
    plt.xlabel('c')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Knapsack - Greedy')
    plt.show()

plotting_instances= []
# greedyplot(plotting_instances)
