
def parse_instance(filepath):
    """This function will parse the knapsack problem instance file at the filepath
    and return a list of [optimum, n, wmax, V:[vi|i=0 to n-1], W:[wi|i=0 to n-1]] 
    with the datatype format [str, int, int, [int] [int]], optimum is left string since right now
    there are blank lines on the first line on some files and casting a blank string in int 
    would cause errors. This is to be dealt in analysis part"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
        optimum = lines[0].strip()
        n, wmax = lines[1].split()
        V = []
        W = []
        for line in lines[1:-1]:
            vi, wi = line.split()
            V.append(int(vi))
            W.append(int(wi))
    return [optimum, int(n), int(wmax), W, V]

