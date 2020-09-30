#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    
    #the nature of this problem is to find the number of spaces a queen on a chessboard can land given n^2 number of squares are k number of obstacles
    #The solution I have here could be made more efficient by leveraging linear algebra and matrices of the objects and squares.  
    #One could take 4 vectors, all passing through the point the queen is on, that represents all potential paths of movement, and define their starts and ends to be the borders of the board or obstacles that block the path
    #Then use the length of the vectors to find the number of open spaces on the board that the queen can move along.
    #This present solution simply walks along 8 vectors originating at the queens location, stopping as soon as it comes across an object or border of the board.
    #8 vectors with r_q as origin, either end of board or obstacle ends the vector.  Eg, 
    #r_q -> edge of board left
    
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

    while upL == True:
        potentialPosition[0] += -1
        potentialPosition[1] += 1
        
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            upL = False
            potentialPosition = [r_q,c_q]
        
        else: 
            numAttacks += 1        

    while upR == True:
        
        potentialPosition[0] += 1
        potentialPosition[1] += 1
    
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            upR = False
            potentialPosition = [r_q,c_q]
            
        else: 
            numAttacks += 1

    while left == True:
        
        potentialPosition[0] += -1
        
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            left = False
            potentialPosition = [r_q,c_q]
           
        else: 
            numAttacks += 1
   

    while right == True:
        potentialPosition[0] += 1
       
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            right = False
            potentialPosition = [r_q,c_q]
          
        else: 
            numAttacks += 1
          

    while downL == True:
        potentialPosition[0] += -1
        potentialPosition[1] += -1
        
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            downL = False
            potentialPosition = [r_q,c_q]
               
        else: 
            numAttacks += 1
          
      
    while downR == True:

        potentialPosition[0] += 1
        potentialPosition[1] += -1
       
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            downR = False
            potentialPosition = [r_q,c_q]
              
        else: 
            numAttacks += 1
    
    
    while down == True:
        potentialPosition[1] += -1
       
        print(potentialPosition)
        if (potentialPosition in obstacles) or (n+1 in potentialPosition) or (0 in potentialPosition):
            down = False
            potentialPosition = [r_q,c_q]
               
        else: 
            numAttacks += 1
           
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
