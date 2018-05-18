# -*- coding: utf-8 -*-
"""
Ratiorg got statues of different sizes as a present from
 CodeMaster for his birthday, each statue having an non-negative integer size.
 Since he likes to make things perfect, he wants to arrange them from 
 smallest to largest so that each statue will be bigger than the previous 
 one exactly by 1. He may need some additional statues to be able to accomplish 
 that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.

@author: hypatiad
"""
def makeArrayConsecutive2(statues):
    import numpy as np
    statues=np.array(statues)
    statues=np.sort(statues)
    diff=tuple(statues[i+1]-statues[i]-1 for i in range(len(statues)-1))
    n=np.sum(diff)
    for i in range(len(statues)):
         if 0<=statues[i]<=20:
            return(n)
                  
