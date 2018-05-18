"""
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first 
half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.

Example
For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.

@author:hypatiad
"""
def isLucky(n):
    count=len(str(n))
    #since we use remainder for the second half,this is a quick 
    #fix for tracking 0 digits is to introduce a string
    nw=str(n)
    sum2=[0] 
    sum1=0
    for i in range(1,(count//2)+1):
        num1=n//10**(count-i)
        if num1>=10:
            num1=num1%10
        sum1=sum1+num1
        num2=n%10**(i)
        while num2>=10:
            num2=num2//10
        sum2.append(num2) 
         #avoid double counting if there is 0 value as a digit
        if nw.find('0')>0:
            sum2tot=sum(set(sum2))
        else:
            sum2tot=sum(sum2)
    return(sum1==sum2tot)
