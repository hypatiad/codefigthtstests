# -*- coding: utf-8 -*-
"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.

@author: hypatiad
def centuryFromYear(year):
    import math
    if 1<=year<=2005:
       if math.ceil(year/100)==math.floor(year/100):
          century=int(year/100)
       else:
           century=int(year/100)+1
   
    return century

