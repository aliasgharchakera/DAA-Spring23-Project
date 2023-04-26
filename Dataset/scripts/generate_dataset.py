import os
from generate_single_instance import very_large_n, very_large_wmax, very_large_n_and_wmax,  very_large_valued_V, very_large_valued_W, very_large_valued_V_and_W
from sys import path
path.append("../../Algorithms/")
# from knapsack_dp import knapsack_dp


BASE_GROUP_PATH = "../base_group/"
FILENAMES_PATH = "./filenames.txt"


def generate_instances(dataset_group, num_instances, folder_name, arguments):
    """
    This function takes a function "dataset_group" as an input, the function
    "dataset_group" should generate a new instance of the dataset when provided
    with n, c, d, and k as inputs This function runs the function provided as
    argument num_instances times, and saves the generated instances in the
    folder named on "dataset_group" string
    """
    directory_path = "../" + folder_name
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    for i in range(num_instances):
        instance = dataset_group(arguments)
        # if i%100==0:
            # print(instance[0], instance[1], len(instance[2]), len(instance[3]))
        # instance is a list with first two arguments as int and the other two
        # arguments as lists now we have to open a file in the folder named on
        # dataset_group and save the instance in it
        file_path = directory_path + "/instance_" + \
            "0"*(4-len(str(i))) + str(i) + ".txt"
        with open(file_path, "w") as f:
            # f.write(str(knapsack_dp(instance[1], instance[3], instance[2], instance[0]))+"\n")
            # If you want only blank line, uncomment the below one and comment above one
            # Not doing this takes a veryyyyy long time that you don't need to spend, 
            # since it'll then run dp on every instance which are 6000
            # f.write("\n")
            f.write(str(instance[0]) + " " + str(instance[1]) + "\n")
            # for ci, vi in zip(instance[2], instance[3]):
            # assert(len(instance[2])==instance[0])
            for i in range(instance[0]):
                ci = instance[2][i]
                vi = instance[3][i]
                f.write(str(vi) + " " + str(ci) + "\n")


def main():
    generate_instances(very_large_n, 100, 'very_large_n_group', [
                       1000, 2000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_wmax, 100, 'very_large_wmax_group', [
        5000, 10000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_n_and_wmax, 100, 'very_large_n_and_wmax_group', [
        1000, 2000, 5000, 10000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_valued_V, 100, 'very_large_valued_V_group', [
        2000, 3000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_valued_W, 100, 'very_large_valued_W_group', [
        1000, 2000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_valued_V_and_W, 100, 'very_large_valued_V_and_W_group', [
        2000, 3000, 1000, 2000, BASE_GROUP_PATH, FILENAMES_PATH])


main()