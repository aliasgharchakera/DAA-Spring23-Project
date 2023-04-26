import random
import statistics
import matplotlib.pyplot as plt
import selection_scheme as ss

class KnapSack:

    def __init__(self, items:list, N, capacity, n) -> None:
        '''
        Constructor for class knapsack. Reads the file and populate items
        '''
        # self.items = list()  #(weight, value)
        # with open(filepath) as f:
        #     lines = f.readlines()
        #     self.num, self.capacity = lines[0].split()
        #     self.num, self.capacity = int(self.num), int(self.capacity)
        #     for i in lines[1::]:
        #         value, weight = i.split()
                # self.items.append((int(value), int(weight)))
        # print(len(self.items))
        self.items = items
        self.num = N
        self.capacity = capacity
        self.numItems = len(self.items)
        self.population = self.generatePopulation(n)
        # print(self.population)

    def generatePopulation(self,n:int):
        '''
        Generates population for the knapsack problem. 
        '''
        population = dict()
        for i in range(n):
            lstItems = [(0,0) for i in range(self.numItems)]
            weight = 0
            value  = 0
            randomNum = random.randint(0,self.numItems-1)
            selectItem = self.items[randomNum]
            while(weight + selectItem[1] <= self.capacity):
                lstItems[randomNum] = selectItem
                weight += selectItem[1]
                value += selectItem[0]
                randomNum = random.randint(0,self.numItems-1)
                selectItem = self.items[randomNum]
            population[value] = lstItems
        return population

    def selectParents(self, selectionChoice:str):

        if selectionChoice == 'binaryTournament':
            firstParent = ss.binaryTournament(self.population)
            secondParent = ss.binaryTournament(self.population)

        elif selectionChoice == 'fitnessProportional':
            parents = ss.fitnessProportionalSelection(self.population, 3, True)
            firstParent = parents[0]
            secondParent = parents[1]

        elif selectionChoice == 'rankBase':
            pass

        return firstParent, secondParent

    def crossOver(self):

        parents = self.selectParents('binaryTournament')
        
        firstParent = self.population[parents[0]]
        secondParent = self.population[parents[1]]

        offSpringDetails = self.createOffSpring(firstParent, secondParent, False)
        self.population[offSpringDetails[0]] = offSpringDetails[1]

        offSpringDetails2 = self.createOffSpring(firstParent, secondParent, True)
        self.population[offSpringDetails2[0]] = offSpringDetails2[1]

    def createOffSpring(self, firstParent, secondParent, swap):
        
        offSpring1 = [(0,0) for i in range(self.num)]
        weight1 = 0
        visited = []

        if (swap == True):
            _firstParent = secondParent
            _secondParent = firstParent
        else:
            _firstParent = firstParent
            _secondParent = secondParent

        for i in range(len(firstParent)//2):
            if (_firstParent[i][1] + weight1 <= self.capacity and _firstParent[i] not in visited):
                visited.append(_firstParent[i])
                offSpring1[i] = _firstParent[i]
                weight1 += _firstParent[i][1]

        i = len(firstParent) // 2
        for j in range(len(firstParent)//2):
            if (_secondParent[i+j][1] + weight1 <= self.capacity and _secondParent[i+j] not in visited):
                visited.append(_secondParent[i+j])
                offSpring1[i+j] = _secondParent[i+j]
                weight1 += _secondParent[i+j][1]
        
        for i in range(len(firstParent)//2):
            if (_secondParent[i][1] + weight1 <= self.capacity and _secondParent[i] not in visited):
                visited.append(_secondParent[i])
                offSpring1[i] = _secondParent[i]
                weight1 += _secondParent[i][1]
 
        i = len(firstParent) // 2
        for j in range(len(firstParent)//2):
            if (_firstParent[i+j][1] + weight1 <= self.capacity and _firstParent[i+j] not in visited):
                visited.append(_firstParent[i+j])
                offSpring1[i+j] = _firstParent[i+j]
                weight1 += _firstParent[i+j][1]        

        return weight1, offSpring1

        
    def calculateFitness(self):
        return list(self.population.keys())
        
    def survivalSelection(self, selectionChoice:str):

        if selectionChoice == 'truncation':
            self.population = ss.truncation(self.population,30, True)
        
        elif selectionChoice == 'fitnessProportional':
            pass

        elif selectionChoice == 'rankBase':
            ss.rankBaseSelection(self.population,30, False)
      
    def getFitness(self):
        return list(self.population.keys())
        
def run(items, n, c, pop, gen, iteration):
    bruh = KnapSack(items, n, c, pop)
    minlst, avglst, avgminlst, avgavglst = list(), list(), list(), list()
    for iteration in range(iteration):
        bruh.generatePopulation(pop)
        for generation in range(gen):
            for offspring in range(5):
                bruh.crossOver()
            bruh.survivalSelection('truncation')
            # print('Max: ',max(bruh.getFitness()))
            minlst.append(max(bruh.getFitness()))
            avglst.append(statistics.mean(bruh.getFitness()))
            # print('Avg: ',statistics.mean(bruh.getFitness()))
        avgminlst.append(statistics.mean(minlst))
        avgavglst.append(statistics.mean(avglst))
    # return minlst, avglst
    # print('Max: ',max(minlst))
    return max(minlst)
    # for i in range(10):
    #     for i in range(1000):
    #         for i in range(5):
    #             bruh.crossOver()
    #         bruh.survivalSelection('truncation')
    # print(bruh.calculateFitness())
    

import os
from sys import path
path.append("../../Dataset/")
import time
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

def kill_time():
    time.sleep(1)
# with timer("func"):
#     kill_time()
    
    
# def main():
#     categories = ["very_large_n", "very_large_wmax", "very_large_n_and_wmax",  "very_large_valued_V", "very_large_valued_W", "very_large_valued_V_and_W"]
#     instances = 3
#     iterations = 3
#     avg_score = list()
#     avg_time = list()
#     n_lst = list()
#     c_lst = list()
#     for c in categories:
#         for i in range(instances):
#             score = list()
#             timelst = list()
#             num = "0"
#             if i < 10:
#                 num += "00"
#             elif i < 100:
#                 num += "0"
#             location = f"../../Dataset/{c}_group/instance_{num}{i}.txt"
#             items = list()
#             with open(location) as f:
#                 lines = f.readlines()
#                 num, capacity = lines[0].split()
#                 num, capacity = int(num), int(capacity)
#                 for i in lines[1::]:
#                     value, weight = i.split()
#                     items.append((int(value), int(weight)))
#             for i in range(iterations):
#                 with timer("func", timelst):
#                     max = run(items, num, capacity, 30, 50, 1)
#                 score.append(max)
#             n_lst.append(num)
#             c_lst.append(capacity)
#             avg_score.append(statistics.mean(score))
#             avg_time.append(statistics.mean(timelst))
#     with open('analysis.csv', 'w') as f:
#         f.write("score, time\n")
#         for i in range(instances*len(categories)):
#             if i % instances == 0:
#                 f.write(f"{categories[i//instances]}\n")
#             f.write(f"{avg_score[i]}, {avg_time[i]}\n")
    
#     plt.plot(avg_score, avg_time, label="max")
#     plt.show()

# main()
def main():
    categories = ["very_large_n"]
    instances = 100
    iterations = 3
    avg_score = list(); avg_time = list()
    n_lst = list(); c_lst = list()
    for c in categories:
        for i in range(instances):
            score = list()
            timelst = list()
            
            num = "0"*(4-len(str(i)))
            # if i < 10:
            #     num += "00"
            # elif i < 100:
            #     num += "0"
            location = f"../../Dataset/{c}_group/instance_{num}{i}.txt"
            items = list()
            with open(location) as f:
                lines = f.readlines()
                num, capacity = lines[0].split()
                num, capacity = int(num), int(capacity)
                for i in lines[1::]:
                    value, weight = i.split()
                    items.append((int(value), int(weight)))
                    
            for i in range(iterations):
                with timer("func", timelst):
                    max = run(items, num, capacity, 30, 50, 1)
                score.append(max)
            n_lst.append(num)
            c_lst.append(capacity)
            avg_score.append(statistics.mean(score))
            avg_time.append(statistics.mean(timelst))
            n_t = list(zip(n_lst, avg_time))
            n_t.sort(key=lambda x: x[0])
            # n_t is a list of tuples of (n, time), I want two separate lists of n and time
            n_list, time_list = zip(*n_t)
    with open('analysis.csv', 'w') as f:
        f.write("score, time\n")
        for i in range(instances*len(categories)):
            if i % instances == 0:
                f.write(f"{categories[i//instances]}\n")
            f.write(f"{avg_score[i]}, {avg_time[i]}\n")
    
    plt.plot(n_list, time_list, label="max")
    plt.show()

main()


# minlst, avglst = run()
# plt.plot([i for i in range(1, 41)], minlst, label="max")
# plt.plot([i for i in range(1, 41)], avglst, label="avg")
# plt.xlabel('generation')
# plt.title('Plot of average fitness against generations')
# # plt.xlabel('iteration')
# # plt.title('Plot of average fitness against iterations')
# plt.ylabel('fitness')
# plt.legend()
# plt.show()
