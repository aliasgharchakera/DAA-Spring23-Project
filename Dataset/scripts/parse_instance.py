
def parse_instance(filepath):
    """This function will parse the knapsack problem instance file at the filepath
    and return a list of [c, n, C:[ci|i=0 to n-1], V:[vi|i=0 to n-1]] with the
    datatype format [int, int, [int] [int]]"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
        n, wmax = lines[1].split()
        V = []
        W = []
        for nm, line in enumerate(lines[2:-2]):
            if "0 1 0 0 0" in line:
                print(nm, filepath, "oe pagal hgya re ye")
            vi, wi = line.split()
            V.append(int(vi))
            W.append(int(wi))
    return [int(n), int(wmax), V, W]
