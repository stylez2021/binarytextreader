def solution(m):
    #​ My​ ​code​ ​here
    from math import gcd
    print("Greatest common D:", gcd(2,9))

    #array of arrays
    fuelCell1 = []
    #print(m)
    for x in m:
        fuelCell1.append(x)



    #print("F this Cell:")
    #for f in fuelCell1:
    #    print(f)
    #print([0, 0, 0, 0, 0])


solution([["penis"],["balls"],["boobies"]])
#solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])

# The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state.
# That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during
# the calculation, as long as the fraction is simplified regularly.

# Input:
# solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# Output:    [7, 6, 8, 21]

# Input:
# solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:    [0, 3, 2, 9, 14]