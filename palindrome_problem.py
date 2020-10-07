#!/bin/python3

import os
import sys

#
# Complete the buildPalindrome function below.
#
def buildPalindrome(a, b):
    
    reverseB = b.reverse()
    symmetricPointList = []
    helperHalfString = ""
    for elementNum in range(len(a)):
        intraCount = 1
        interCount = 1
        intraSymmetryCheck = True
        interSymmetryCheck = True
        while intraSymmetryCheck == True:
            if a[elementNum - intraCount] == a[elementNum + intraCount]:
                intraCount += 1 
                symmetricPointList.append([elementNum, intraCount, "odd", "intra"])
            if a[elementNum -intraCount] == a[elementNum]:
                symmetricPointList.append([elementNum, intraCount, "even", "intra"])
            else: intraSymmetryCheck = False
        while interSymmetryCheck == True:
            if a[elementNum-interCount:elementNum] in reverseB:
                interCount += 1
                symmetricPointList.append[elementNum, interCount, "odd", "inter"]
            if a[elementNum-interCount:elementNum-1] in reverseB:
                interCount +=1
                symmetricPointList.append([elementNum, interCount, "even", "inter"])
            else: interSymmetryCheck = False
    
    #Each middle point of every palendrome should be stored in symmetricPointList
    #each palendrome with the center being within a string, rather than at the end of a substring, now has to be checked for inter string symmetry; what's beyond the left or right end must be compared to the other string for overlap
    
    #Suffix tree solution might work better
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()
