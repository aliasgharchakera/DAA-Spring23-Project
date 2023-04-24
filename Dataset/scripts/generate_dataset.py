import os
from generate_single_instance import very_large_n, very_large_wmax, very_large_n_and_wmax,  very_large_valued_V, very_large_valued_W, very_large_valued_V_and_W

BASE_GROUP_PATH = "../base_group/"
FILENAMES_PATH = "../filenames.txt"


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
        # instance is a list with first two arguments as int and the other two
        # arguments as lists now we have to open a file in the folder named on
        # dataset_group and save the instance in it
        file_path = directory_path + "/instance_" + \
            "0"*(4-len(str(i))) + str(i) + ".txt"
        with open(file_path, "w") as f:
            f.write(str(instance[0]) + " " + str(instance[1]) + "\n")
            for ci, vi in zip(instance[2], instance[3]):
                f.write(str(ci) + " " + str(vi) + "\n")


def main():
    generate_instances(very_large_n, 1000, 'very_large_n_group', [
                       750, 1250, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_wmax, 1000, 'very_large_wmax_group', [
        1000, 3000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_n_and_wmax, 1000, 'very_large_n_and_wmax_group', [
        750, 1250, 3000, 5000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_valued_V, 1000, 'very_large_valued_V_group', [
        5000, 10000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_valued_W, 1000, 'very_large_valued_W_group', [
        5000, 10000, BASE_GROUP_PATH, FILENAMES_PATH])
    generate_instances(very_large_valued_V_and_W, 1000, 'very_large_valued_V_and_W_group', [
        5000, 10000, 5000, 10000, BASE_GROUP_PATH, FILENAMES_PATH])


main()
