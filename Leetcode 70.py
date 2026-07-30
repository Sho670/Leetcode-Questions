# Leetcode 70 (Climbing Stairs).

# Time complexity: O(n).

# Optimization Used: Dynamic Programming.

class Solution:
  def climbingstairs(self, nums-> int):

    dp= [-1]*(n+1)

    def f(n):
      
      if (n==0):
        return 1
        
      if (n<0):
        return 0
        
      if (dp[n]!=-1):
        return dp[n]

    dp[n]=f(n-1)+f(n-2)

    return dp[n]

    return f(n)
    
    
