"""
Given two strings, find the number of common characters between them.

Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".

@author: hypatiad
"""
def commonCharacterCount(s1, s2):
    from collections import Counter
    cnt=0
    l1=len(s1)
    l2=len(s2)
    words=list()
    indmin=min(l1,l2)
    indmax=max(l1,l2)
    for i in range(indmin):
        w1=s1[i]
        counter1=Counter(s1)#how many times character occured in a string
        counter2=Counter(s2)            
        if  w1 in s2 and counter1[w1]<=counter2[w1]:
            cnt=cnt+1  
            words.append(w1)
        elif w1 in s2 and counter1[w1]>counter2[w1]:
            if  w1 not in words:
                cnt=cnt+1
                words.append(w1)
    if indmax>l1:
        for j in range(indmin, indmax-1):
            w1=s2[j]
            if w1 in s1 and w1 not in words:
                words.append(w1)
                cnt=cnt+1
                j=j+1
    return(cnt)   

