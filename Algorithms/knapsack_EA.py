import random
from EA import Knapsack
def evolutionaryAlgorithm(items, num, capacity):
    fitnessEvaluation = dict()
    for iteration in range(1):

        # print("***** Iteration Number = " + str(iteration+1) + " *****")

        k1 = Knapsack(items, num, capacity)

        k1.goodPopulate()
        # t1.calculateFitness()
        # g1.populate()
        # g1.calculateFitness()

        for generation in range(k1.numOfGenerations):
            # print("***** Iteration Number = " + str(iteration+1) + ", Generation Number = " + str(generation+1) + " *****")

            totalOffsprings = []

            for i in range(5):
                # parents = k1.randomSelection(0)
                # parents = k1.fpsSelection(0)
                # parents = k1.rbsSelection(0)
                # parents = k1.truncation(0)
                parents = k1.binarySelection(0)

                p1 = parents[0]
                p2 = parents[1]

                offsprings = k1.crossover(p1, p2)
                for j in range(2):
                    randomNumber = random.randint(0,1)
                    if randomNumber == 1:

                        tempOffspring = k1.mutation(offsprings[j])

                        offsprings[j] = tempOffspring

                    offspring = k1.newFitness(offsprings[j])

                    totalOffsprings.append(offspring)
            
            for i in totalOffsprings:
                k1.population.append(i)

            # k1.randomSelection(1)
            # k1.fpsSelection(1)
            k1.rbsSelection(1)
            # k1.truncation(1)
            # k1.binarySelection(1)

            max = k1.generationEvaluation()
        k1.iterationEvaluation(fitnessEvaluation,iteration)
        return max
    # k1.plotGraphs(fitnessEvaluation)
  
# knapsackFile = 'f8_l-d_kp_23_10000'
# tspFile ='qa194.tsp'
# graphFile = 'gcol1.txt'

# evolutionaryAlgorithm(items)


import os
from sys import path
path.append("../Dataset/")
import time
import statistics
import matplotlib.pyplot as plt
from contextlib import contextmanager

@contextmanager
def timer(label: str, timelst):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        # print(f"{label}: {end - start:.3f} seconds")
        timelst.append(end-start)
        
def main(plotting_instances):
    categories = ["very_large_n"]
    instances = 100
    iterations = 3
    avg_score = list(); avg_time = list()
    n_lst = list(); c_lst = list()
    w_lst = list(); v_lst = list()
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
                    items.append([int(value), int(weight)])
                    W.append(int(weight)); V.append(int(value))
                    
            for i in range(iterations):
                with timer("func", timelst):
                    max = evolutionaryAlgorithm(items, num, capacity)
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
                    max = evolutionaryAlgorithm(items, num, capacity)
                score.append(max)
            n_lst.append(num)
            c_lst.append(capacity)
            avg_score.append(statistics.mean(score))
            avg_time.append(statistics.mean(timelst))
            c_t = list(zip(c_lst, avg_time))
            c_t.sort(key=lambda x: x[0])
            # n_t is a list of tuples of (n, time), I want two separate lists of n and time
            c_list, time_list = zip(*c_t)
    with open('analysis4.csv', 'w') as f:
        f.write("score, time\n")
        for i in range(instances*len(categories)):
            if i % instances == 0:
                f.write(f"{categories[i//instances]}\n")
            f.write(f"{avg_score[i]}, {avg_time[i]}\n")
    
    plotting_instances.append((c_list, time_list))
    return plotting_instances


# def main():
#     vlargen()
#     wmax()
#     # print(plotting_instances)
#     for data in plotting_instances:
#         plt.plot(data[0], data[1], color='blue', label="")
#     plt.xlabel('c')
#     plt.ylabel('Time (seconds)')
#     plt.legend()
#     plt.title('Knapsack - EA')
#     plt.show()

# main()

def eaplot(plotting_instances = []):
    # plotting_instances = []
    plotting_instances.append(main(plotting_instances))
    # wmax(plotting_instances)
    # vlargev()
    # print(plotting_instances)
    for data in plotting_instances:
        plt.plot(data[0], data[1], color='blue', label="")
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Knapsack - EA')
    plt.show()

plotting_instances = []
# eaplot(plotting_instances)
