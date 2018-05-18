# -*- coding: utf-8 -*-
"""
Given an array of integers, find the pair of adjacent elements that has the 
largest product and return that product.
Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21
An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.
@author: hypatiad
"""
def adjacentElementsProduct(inputArray):
   if 2<=len(inputArray)<=10:
      t=tuple(inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1))
      maxt=max(t)
      for i in range(len(inputArray)-1): 
          if -1000<=inputArray[i]<=1000:
            return(maxt)
            