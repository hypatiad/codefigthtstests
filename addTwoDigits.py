'''You are given a two-digit integer n. Return the sum of its digits.
Example: For n = 29, the output should be
addTwoDigits(n) = 11.'''
def addTwoDigits(n):
  sum2=0
  num1=n//10
  num2=n%10
  sum2=num1+num2
  return(sum2)
