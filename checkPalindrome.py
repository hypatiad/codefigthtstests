# -*- coding: utf-8 -*-
"""
Given the string, check if it is a palindrome.

For inputString = "ana", the output should be
checkPalindrome(inputString) = true;
For inputString = "tata", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
@author: hypatiad
"""
def checkPalindrome(inputString):
    if 1<=len(inputString)<=1E5:
           revString=inputString[::-1]
    return(revString==inputString)
      