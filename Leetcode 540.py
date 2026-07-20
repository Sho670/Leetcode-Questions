# Leetcode Question 540 (Fibonacci Number)

def fibonacci(self, n):

  dp = [-1]*(n+1)

  def f(n):
    if (n==0):
      return 0
    if (n==1):
      return 1
