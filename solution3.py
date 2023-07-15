def solution(xs):
    #my code here
    powerArray = []

    print(xs)
    for num in xs:
        print(num)
        if num != 0:
            powerArray.append(num)

    print(powerArray)

    #times the numbers in the powerArray by themselfs and print the total?
    result = 1 
    for x in powerArray:
        result = result * x
    print(result)


solution([2, 0, 2, 2, 0])

# You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount
# of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is.
# Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns
# the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of
# [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.
# So solution([2,-3,1,0,-5]) will be "30".


#print(a string)

# Input:
# solution.solution([2, 0, 2, 2, 0])
# Output:    8

# Input:
# solution.solution([-2, -3, 4, -5])
# Output:    60