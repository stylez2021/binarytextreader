def solution(area):
    #my code here
    import math

    #think squares
    #OK so the largest square I can make with 12 is:
    #9 : 3x3 square and then 3 smaller squares, hence the final output; [9, 1, 1, 1]
    #16: 4x4 square
    #18: [16, 1, 1]
    
    # there's probably a simple math solution for this but dang it's been a while
    
    #Divide this number by 9
    #but then if the mod is less than 9 divide it into individual 'squares'

    #setting up final array to be returned here:
    output = []  

    #Determine if a number can be squared, otherwise ... do something else
    #o = area
    global area2
    area2 = area
    #print(area2)
    def isSquare():
        global area2
        o = area2
        while o > 0:
            sqr = math.sqrt(o)
            if int(sqr + 0.5) ** 2 == o:
                #print(o, "is square")
                output.append(o)
                area2 -= o
                #print("Area is now", area2)
                break
            elif o == 0:
                area2 = 0
            else:
                #print(o, "ain't square")
                o -= 1

    while area2 > 0:
        isSquare()

    #convert to string output I guess
    str1 = ""
    for i in output:
        str1 += str(i) + ","
    print(str1[:-1])
    #print(output)



#solution(12)
solution(15324)
