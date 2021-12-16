#The codes from the algorithms are from 142_binpacking.py with a lot of modifications
#to store the elements in each bin
#Maximize the window to display text and graphs properly

import numpy as np
import matplotlib.pyplot as plt


def nextFit(weight, cap):
    res = 1
    rem = cap
    bins = []
    curr_bin = []
    for x in range(len(weight)):        
        if rem >= weight[x]:
            rem = rem - weight[x]
            curr_bin.append(weight[x])
            if(x == (len(weight) - 1)):
                bins.append(curr_bin)
        else:
            bins.append(curr_bin)
            curr_bin = []
            res += 1
            rem = cap - weight[x]
            curr_bin.append(weight[x])
            if(x == (len(weight) - 1)):
                curr_bin = []
                curr_bin.append(weight[x])
                bins.append(curr_bin)
    result = [res, bins]
    return result

def nextFitDec(weight, cap):
    sorted_weights = sorted(weight)
    sorted_weights.reverse()
    result = nextFit(sorted_weights, cap)
    return result

def firstFit(weight, cap):
    bins = 0
    n = len(weight)
    bin_cap = [0]*n
    bin_contents = []
    
    for x in range(n):
        y = 0
        while(y < bins):
            if(bin_cap[y] >= weight[x]):
                bin_cap[y] -= weight[x]
                bin_contents[y].append(weight[x])
                break
            else:
                y += 1
    
        if(y == bins):
            bin_cap[bins] = cap - weight[x]
            bin_contents.append([])
            bin_contents[y].append(weight[x])
            bins += 1
    
    result = [bins, bin_contents]
    return result

def firstFitDec(weight, cap):
    sorted_weights = sorted(weight)
    sorted_weights.reverse()
    result = firstFit(sorted_weights, cap)
    return result


def label_xticks(result):
    bins = result[0]
    bin_contents = result[1]
    rem_current = 0
    rem = [0]*bins
    xticks = []
    labels = [0]*bins
    for i in range(bins):
        rem[i] = cap - sum(bin_contents[i])
    for j in range(bins):
        labels[j] = str(j)
    xticks = [f"Rem: {i}" for i in rem]
    return labels, xticks

def data(weight, result):
    bins = result[0]
    bin_contents = result[1]
    labels = []
    for i in range(bins):
        rem = str((cap - sum(bin_contents[i])))
        label  = f"Rem: {rem}"
        labels.append(label)
    items = []
    current_items = []

    bin_items = result[1]
    bin_len = [len(i) for i in bin_items]
    max_bin_len = max(bin_len)
    for x in range(max_bin_len):
        current_items = []
        for y in range(bins):
            if not x >= len(bin_items[y]):
                current_items.append(bin_items[y][x])
            else:
                current_items.append(0)
        items.append([])
        items[x] = current_items
    print(items)
    return items

def printBins(weight, cap):
    width = 0.35
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.tick_params(axis='y', labelsize=8)
    ax1.set_xlabel("Next Fit Algorithm")

    ax2.tick_params(axis='y', labelsize=8)
    ax2.set_xlabel("First Fit Algorithm")

    ax3.tick_params(axis='y', labelsize=8)
    ax3.set_xlabel("Next Fit Decreasing Algorithm")

    ax4.tick_params(axis='y', labelsize=8)
    ax4.set_xlabel("First Fit Decreasing Algorithm")

    #   NextFit    
    result = nextFit(weight, cap)
    items = data(weight, result)
    labels, xticks = label_xticks(result)
    ax1.set_title(f"Bins: {result[0]}, Contents: {result[1]}")
    bot = items[0]
    for x in range(len(items)):
        if (x == 0):
            ax1.bar(labels, items[x], width, color="yellow", edgecolor="black")
        else:
            ax1.bar(labels, items[x], width, color="yellow", edgecolor="black", bottom=bot)
            bot = np.add(bot, items[x])
    ax1.set_xticklabels(xticks)


    #   FirstFit
    result = firstFit(weight, cap)
    items = data(weight, result)
    labels, xticks = label_xticks(result)
    ax2.set_title(f"Bins: {result[0]}, Contents: {result[1]}")
    bot = items[0]
    for x in range(len(items)):
        if (x == 0):
            ax2.bar(labels, items[x], width, color="yellow", edgecolor="black")
        else:
            ax2.bar(labels, items[x], width, color="yellow", edgecolor="black", bottom=bot)
            bot = np.add(bot, items[x])
    ax2.set_xticklabels(xticks)

    #   NextFit Decreasing
    result = nextFitDec(weight, cap)
    items = data(weight, result)
    labels, xticks = label_xticks(result)
    ax3.set_title(f"Bins: {result[0]}, Contents: {result[1]}")
    bot = items[0]
    for x in range(len(items)):
        if (x == 0):
            ax3.bar(labels, items[x], width, color="yellow", edgecolor="black")
        else:
            ax3.bar(labels, items[x], width, color="yellow", edgecolor="black", bottom=bot)
            # bot = np.add(bot, items[x])
            bot = [a+b for a, b in zip(bot, items[x])]
    ax3.set_xticklabels(xticks)

    #   FirstFit Decreasing
    result = firstFitDec(weight, cap)
    items = data(weight, result)
    labels, xticks = label_xticks(result)
    # labels = ["1", "2", "3", "4"]
    ax4.set_title(f"Bins: {result[0]}, Contents: {result[1]}")
    bot = items[0]
    for x in range(len(items)):
        if (x == 0):
            ax4.bar(labels, items[x], width, color="yellow", edgecolor="black")
        else:
            ax4.bar(labels, items[x], width, color="yellow", edgecolor="black", bottom=bot)
            bot = np.add(bot, items[x])            
    ax4.set_xticklabels(xticks)
    
    fig.tight_layout()
    fig.suptitle(f"weights: {weight}\n", fontweight='bold')
    plt.setp((ax1, ax2, ax3, ax4), yticks=np.arange(0, cap + 1, 1))
    plt.show()
    


    
# pls limit the cap to 20
#Test Case 1
weight = [2, 5, 4, 7, 1, 3, 8]
cap = 10
#Test Case 2
# weight = [10, 3, 16, 5, 4, 12, 7, 15]
# cap = 20
printBins(weight, cap)
