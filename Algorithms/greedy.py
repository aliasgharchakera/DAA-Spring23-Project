# Calculate the ratio (profit/weight) for each item.
# Sort all the items in decreasing order of the ratio.
# Initialize res = 0, curr_cap = given_cap.
# Do the following for every item i in the sorted order:
# If the weight of the current item is less than or equal to the remaining capacity then add the value of that item into the result
# Else add the current item as much as we can and break out of the loop.
# Return res.



# Structure for an item which stores weight and
# corresponding value of Item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
 
# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
 
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)   
 
    # Result(value in Knapsack)
    finalvalue = 0.0
 
    # Looping through all Items
    for item in arr:
 
        # If adding Item won't overflow,
        # add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
 
        # If we can't add current Item,
        # add fractional part of it
        else:
            finalvalue += item.profit * W / item.weight
            break
     
    # Returning final value
    return finalvalue
 
 
# Driver Code
if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
 
    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
