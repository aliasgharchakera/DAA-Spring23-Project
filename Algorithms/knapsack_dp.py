# This algorithm is taken from
# [GeekforGeeks](https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/)


def knapsack_dp(wmax, W, V, n):
    ''' A Dynamic Programming based Python Program for 0-1 Knapsack problem Returns
    the maximum value that can be put in a knapsack of capacity wmax '''
    K = [[0 for x in range(wmax + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for wi in range(wmax + 1):
            if i == 0 or wi == 0:
                K[i][wi] = 0
            elif W[i-1] <= wi:
                K[i][wi] = max(V[i-1] + K[i-1][wi-W[i-1]],  K[i-1][wi])
            else:
                K[i][wi] = K[i-1][wi]

    return K[n][wmax]
