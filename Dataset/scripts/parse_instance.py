
def parse_instance(filepath):
    """This function will parse the knapsack problem instance file at the filepath
    and return a list of [optimum, n, wmax, V:[vi|i=0 to n-1], W:[wi|i=0 to n-1]] 
    with the datatype format [int, int, int, [int] [int]]"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
        optimum = lines[0].strip()
        n, wmax = lines[1].split()
        V = []
        W = []
        for line in lines[2:-2]:
            vi, wi = line.split()
            V.append(int(vi))
            W.append(int(wi))
    return [int(optimum), int(n), int(wmax), V, W]
