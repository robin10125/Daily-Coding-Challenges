#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    #queenPosition = [r_q, c_q]
    closestUpperIntersect = n + 1
    closestLowerIntersect = 0
    #vertical vector closest intersect
    for eachSquare in obstacles:
        if eachSquare[0] == r_q and eachSquare[1] < closestUpperIntersect and eachSquare[1] - c_q > 0:
            closestUpperIntersect = eachSquare[1]
        if eachSquare[0] == r_q and eachSquare[1] > closestLowerIntersect and c_q - eachSquare[1] > 0:
            closestLowerIntersect = eachSquare[1]
    verticalLength = closestUpperIntersect - closestLowerIntersect - 2
    #Number of squares the queen can move to in this line.  
    print(closestLowerIntersect, closestUpperIntersect)

    closestUpperIntersect = n + 1
    closestLowerIntersect = 0   
    #horizontal vector closest intersect
    for eachSquare in obstacles:
        if eachSquare[1] == c_q and eachSquare[0] < closestUpperIntersect and eachSquare[0] - r_q > 0:
            closestUpperIntersect = eachSquare[0]
        if eachSquare[1] == c_q and eachSquare[0] > closestLowerIntersect and r_q - eachSquare[0] > 0:
            closestLowerIntersect = eachSquare[0]
    horizontalLength = closestUpperIntersect - closestLowerIntersect - 2
    print(closestLowerIntersect, closestUpperIntersect)

    closestUpperIntersect = min(n + 1 + (r_q - c_q), n+1)
    closestLowerIntersect = max(r_q - c_q, 0)
    #y=x vector closest intersect  Only x direction is needed, since the queen can only travel along a line of slope 1.
    for eachSquare in obstacles:
        if (eachSquare[0] - eachSquare[1]) == r_q - c_q and (eachSquare[0] - r_q) / (eachSquare[1] -c_q) == 1:
            print("Found y=x")
            if eachSquare[0] < r_q and eachSquare[0] > closestLowerIntersect:
                closestLowerIntersect = eachSquare[0]
            if eachSquare[0] > r_q and eachSquare[0] < closestUpperIntersect:
                closestUpperIntersect = eachSquare[0]
    lineYisXLength = closestUpperIntersect - closestLowerIntersect - 2
    print(closestLowerIntersect, closestUpperIntersect)

    closestUpperIntersect = min(r_q + c_q, n+1)
    closestLowerIntersect = max((r_q + c_q) - n - 1, 0)
    #y=-x vector closest intersect  Only x direction is needed, since the queen can only travel along a line of slope -1.
    for eachSquare in obstacles:
        if (eachSquare[0] + eachSquare[1]) == r_q + c_q and (eachSquare[0] - r_q) / (eachSquare[1] -c_q) == -1:
            print("Found y=-x")
            if eachSquare[0] < r_q and eachSquare[0] > closestLowerIntersect:
                closestLowerIntersect = eachSquare[0]
            if eachSquare[0] > r_q and eachSquare[0] < closestUpperIntersect:
                closestUpperIntersect = eachSquare[0]
    lineYisNegativeXLength = closestUpperIntersect - closestLowerIntersect - 2
    print(closestLowerIntersect, closestUpperIntersect)
    
    totalLength = verticalLength + horizontalLength + lineYisXLength + lineYisNegativeXLength
    print(verticalLength, horizontalLength, lineYisXLength, lineYisNegativeXLength)
    return totalLength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

