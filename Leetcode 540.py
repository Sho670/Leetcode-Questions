# Leetcode Question 540 (Fibonacci Number)


# The question provides a description of finding the fibonocci number of a particular element.

# I am using Dynamic Programming which is nothing but trying to optimize the following code in better way as in it should be on time complexity of O(log n)

def fibonacci(self, n):

  dp = [-1]*(n+1)

  def f(n):
    if (n==0):
      return 0
    if (n==1):
      return 1


    if (dp[n]!= -1):
      return dp[n]

    dp[n]= f(n-1)+ f(n-2)

    return dp[n]

return f(n)
