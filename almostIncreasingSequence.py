# -*- coding: utf-8 -*-
"""
Given a sequence of integers as an array, 
determine whether it is possible to obtain 
a strictly increasing sequence by removing 
no more than one element from the array.
Example
For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;
There is no one element in this array that can be removed in order to get a s
trictly increasing sequence.
For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.
You can remove 3 from the array to get the strictly increasing sequence 
[1, 2]. Alternately, you can remove 2 to get the strictly increasing 
sequence [1, 3].
@author: hypatiad
"""
def almostIncreasingSequence(sequence):
    flag = False

    if(len(sequence) < 3): #only one will be removed [1,3,2] so will be true always
        return True

    if(sequence == sorted(sequence)): #no duplicates
       if(len(sequence)==len(set(sequence))):
           return True

    bigFlag = True #now set real flag
    for i in range(len(sequence)):
        if(bigFlag and i < len(sequence)-1 and sequence[i] < sequence[i+1]):
            bigFlag = True
            continue
        tempSeq = sequence[:i] + sequence[i+1:]
        print(tempSeq)
        if(tempSeq == sorted(tempSeq)):
            if(len(tempSeq)==len(set(tempSeq))):
                flag = True
                break
        bigFlag = False
    return flag
