def solution(x, y):
    #my code here
    import math
    import numpy as np
    solution = ""

    arr = np.tri(5,5)

    print(arr[x, y])

    #print(arr[2])
    
    laIndex = 1
    arrI = 1
    laArr = []
    #ok, sort of got this one going but it's only part 1
    while laIndex < 1000:
        laArr.append(int((laIndex * (laIndex + 1))/2 ))
        laIndex += 1

    print(laArr)
        


# 46
# 37 47
# 29 38 48
# 22 30 39 49 
# 16 23 31 40 50
# 11 17 24 32 41 51 
# 7 12 18 25 33 42 52
# 4 8 13 19 26 34 43 53 
# 2 5 9 14 20 27 35 44 54
# 1 3 6 10 15 21 28 36 45 55

# This can be further simplified as [n(n+1)]/2

# Input:
# solution.solution(5, 10)
# Output:    96

# Input:
# solution.solution(3, 2)
# Output:    9

    #make sure we print out a string
    #print(str(x ** y))

solution(3, 2)