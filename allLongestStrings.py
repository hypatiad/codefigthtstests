"""
Given an array of strings, return another array containing all of its longest 
strings.

Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
@author: hypatiad
"""
def allLongestStrings(inputArray):
   len_w=0
   w=list()
   for i in range(len(inputArray)):
       if len(inputArray[i])>=len_w:
            len_w=len(inputArray[i])
            word=inputArray[i]
            w.append(word)
            j=0
            while j < len(w):
                   if len(w[j])<len(w[len(w)-1]):
                        w.pop(j)
                   else:
                       j+=1
   print(w) 
   return(w)
