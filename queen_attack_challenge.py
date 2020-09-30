#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
#8 vectors with r_q as origin, either end of board or obstacle ends the vector.  Eg, 
    #r_q -> edge of board left
    
    helperCoordinates = [0,0]
    potentialPosition = [r_q, c_q]
    up,upL,upR,left,right,downL,downR,down = True,True,True,True,True,True,True,True
    numAttacks = int(0)
    print("Obstacles = ", obstacles)
    print("Size of board = ", n)
    while up == True:
    
        potentialPosition[1] += 1
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            up = False
            potentialPosition = [r_q,c_q]
            #reset potentialPosition
       
        else: 
            numAttacks += 1 
            print(numAttacks)
    print("End of direction up")

    while upL == True:
        potentialPosition[0] += -1
        potentialPosition[1] += 1
        
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            upL = False
            potentialPosition = [r_q,c_q]
        
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction upL")

    while upR == True:
        
        potentialPosition[0] += 1
        potentialPosition[1] += 1
    
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            upR = False
            potentialPosition = [r_q,c_q]
            
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction upR")

    while left == True:
        
        potentialPosition[0] += -1
        
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            left = False
            potentialPosition = [r_q,c_q]
           
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction left")

    while right == True:
        potentialPosition[0] += 1
       
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            right = False
            potentialPosition = [r_q,c_q]
          
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction right")

    while downL == True:
        potentialPosition[0] += -1
        potentialPosition[1] += -1
        
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            downL = False
            potentialPosition = [r_q,c_q]
               
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction downL")
      
    while downR == True:

        potentialPosition[0] += 1
        potentialPosition[1] += -1
       
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            downR = False
            potentialPosition = [r_q,c_q]
              
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction downR")
    
    while down == True:
        potentialPosition[1] += -1
       
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            down = False
            potentialPosition = [r_q,c_q]
               
        else: 
            numAttacks += 1
            print(numAttacks)
    print("End of direction down")
    return numAttacks

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
