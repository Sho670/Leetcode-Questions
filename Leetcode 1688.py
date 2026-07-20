# Leetcode Question 1688 (Count of matches in tournament)

# The question include the number of matches played by the teams.

class Solution(object):
  
  def numberofmatches(self,num):
    
    if (n==1):
      return 0
      
    if (n%2==0):
      
      return n//2 + self.numberofmatches(n//2)

      
      return (n-1)//2+self.numberofmatches((n-1)//2+1)
