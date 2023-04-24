
def parse_instance(filepath):
    """This function will parse the knapsack problem instance file at the filepath
    and return a list of [c, n, C:[ci|i=0 to n-1], V:[vi|i=0 to n-1]] with the
    datatype format [int, int, [int] [int]]"""
    with open(filepath, 'r') as f:
        c, n = f.readline().split()
        C = []
        V = []
        for line in f:
            ci, vi = line.split()
            C.append(int(ci))
            V.append(int(vi))
    return [int(c), int(n), C, V]
