# Bin Packing Problem and Algorithms
-Benjamin Julien C. Roque
Given an array of n items, with each item having different weights, and an unlimited number of bins of capacity c, assign each item to a bin such that the number of total used bins is minimized.
The weights of the items must be less than or equal to bin capacity c.

## Algorithms
### Next Fit Algorithm
- Time Complexity: O(n)
- Procedues
  - Keeps a current bin
  - Check if element fits inside current bin
  - If element fits, put it inside
  - If element weight > bin remaining capacity, put element inside new bin


### First Fit Algorithm
- Time Complexity: O(n^2). However can be reduced to O(n log n) if binary search tree is used to find bins
- Checks already existsing bins if element fits inside before creating a new bin

