def solution(x, y):
    #my code here
    import math
    import numpy as np
    solution = ""

    
    
    def getVerticleRowNum(thatRow):
        #print("The row detected is", thatRow)
        #print(thatRow + (thatRow - 1))
        return (thatRow + (thatRow - 1))
        
    #Get the offset to add based on the row
    def getRowOffset(Row):
        #print("Calculating offset for row", Row)
        #Math goes here
        #LAWL, the offset is the first row - smacks head ok, how to pull that out
        if Row > 2:
            Row = Row - 2 
            #print("The offset number to add should be",
            return((Row * (Row + 1))/2)
        else:
            print("Row too low no offset addition needed")
            return 0


    getVerticleRowNum(y)
    getRowOffset(y)

    laIndex = 1
    vertRow = 1
    arrI = 1
    laArr = []
    #ok, sort of got this one going but it's only part 1
    while laIndex < 20:
        laArr.append(int((laIndex * (laIndex + vertRow))/2))
        laIndex += 1

    print(laArr)

    #Ok let's strip it down to just the answer now, start with the 1st two rows
    print((int((x * (x + getVerticleRowNum(y)))/2)+getRowOffset(y)))
        

solution(3, 2)


# 46                                  row 19 (+36 needed)
# 37 47                               row 17 (+28 needed)
# 29 38 48                            row 15 (+21 needed)
# 22 30 39 49                         row 13 (+15 needed)
# 16 23 31 40 50                      row 11 (+10 needed)
# 11 17 24 32 41 51                   row 9 (+6 needed)
# 7 12 18 25 33 42 52                 row 7 (+3 needed)
# 4 8 13 19 26 34 43 53               row 5 (+1 needed)
# 2 5 9 14 20 27 35 44 54             row 3 (no mod needed)
# 1 3 6 10 15 21 28 36 45 55          row 1 (no mod needed)

# This can be further simplified as [n(n+1)]/2

# Input:
# solution.solution(5, 10)
# Output:    96

# Input:
# solution.solution(3, 2)
# Output:    9

    #make sure we print out a string
    #print(str(x ** y))