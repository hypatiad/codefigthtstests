'''Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.

Example

For divisor = 3 and bound = 10, the output should be
maxMultiple(divisor, bound) = 9.

The largest integer divisible by 3 and not larger than 10 is 9.'''

    def maxMultiple(divisor, bound):
    import numpy
    a=numpy.arange(1,bound+1)
    b=numpy.zeros(bound+1)
    for i in range(1,bound):
        b[i]=a[i]%divisor
        print(b[i])
        if a[i]<divisor:
            a[i]=0
        if (b[i]!=0):
            a[i]=0
    print(max(a))
    return(max(a))
