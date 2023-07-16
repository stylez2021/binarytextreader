def solution(m):
    #​ My​ ​code​ ​here
    #Nope, not yet:
    #from math import gcd
    #print("Greatest common D:", gcd(2,9))
    #We can use this because they're all the same, no variance
    cellLength = len(m[0])
    #print("Celllength is:", cellLength)
    

    #array of arrays
    fuelCell1 = []
    print(m)
    for x in m:
        fuelCell1.append(x)

    # ok let's find the inner arrays cells that are terminal ones, ie all 0's
    # And we can surmise they're the last rows in the array and do more math with that later
    termArrayCount = 0
    for f in fuelCell1:
        zeroCount = 0
        #print("Print checking row for terminality", f)
        for cell in f:
            if cell == 0:
                zeroCount += 1
        if zeroCount == cellLength:
            termArrayCount += 1
        
    print(str(termArrayCount) + " terminal arrays found.")

        


# solution([["penis"],["balls"],["boobies"]])
solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

# The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state.
# That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during
# the calculation, as long as the fraction is simplified regularly.

# Input:
# solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# Output:    [7, 6, 8, 21]

# Input:
# solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:    [0, 3, 2, 9, 14]