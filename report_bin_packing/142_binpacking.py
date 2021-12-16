#The codes on nextFit and firstFit are based from GeeksForGeeks with slight modifications

def nextFit(weight, cap):
    bins = 1
    rem = cap

    for x in range(len(weight)):
        if(rem >= weight[x]):
            rem -= weight[x]
        else:
            bins += 1
            rem = cap - weight[x]
    return bins

def nextFitDec(weight, cap):
    sorted_weights = sorted(weight)
    sorted_weights.reverse()
    result = nextFit(sorted_weights, cap)
    return result


def firstFit(weight, cap):
    bins = 0
    n = len(weight)
    bin_rem = [0]*n

    for x in range(n):
        y = 0
        while(y < bins):
            if(bin_rem[y] >= weight[x]):
                bin_rem[y] = bin_rem[y] - weight[x]
                break
            y += 1
        
        if(y == bins):
            bin_rem[bins] = cap - weight[x]
            bins = bins + 1
    return bins

def firstFitDec(weight, cap):
    sorted_weights = sorted(weight)
    sorted_weights.reverse()
    result = firstFit(sorted_weights, cap)
    return result

#Test Case 1
weight = [2, 5, 4, 7, 1, 3, 8]
cap = 10
#Test Case 2
# weight = [10, 3, 16, 5, 4, 12, 7, 15]
# cap = 20

print("Weights: ", weight)
print("Number of bins for Next Fit Algorithm: ", nextFit(weight, cap))
print("Number of bins for First Fit Algorithm: ", firstFit(weight, cap))
print("Number of bins for Next Fit Decreasing Algorithm: ", nextFitDec(weight, cap))
print("Number of bins for First Fit Decreasing Algorithm: ", firstFitDec(weight, cap))