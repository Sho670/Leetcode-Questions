# Leetcode Question 53 (Maximum SubArray)

class Solution():
  
  def maxSubArray(self,nums:List[int]):

    marr = max(nums)

    sum=0
    
    for i in nums:
      
      if sum+i>i:
        sum+=i
        
      else:
        sum=i
        
        if sum>marr:
          marr = sum

  return sum


