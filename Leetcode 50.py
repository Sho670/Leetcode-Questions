# Leetcode Question 50 (Pow(x,n))

class Solution(object):
  def myPow(self, x, n):
    if (n<0):
      x=1/x
      n=-n
    if (n==0):
      return 1

    dp = self.myPow(x,n//2)

    if (n%2==0):
      return dp*dp
    return dp*dp*x
