#Leetcode Question 239 (Maximum Sliding Window)

#Problem : Sliding Window

class Solution:
  def maxslidingwindow():
    q=[]
    answer = []
    
    for i in range(len(nums)):
      if q and q[0]< i-k+1:
        q.pop()
      while q and nums[q[-1]<nums[i]]:
        q.pop()

      q.append(i)

      if i>k=1:
          answer.append(nums[q[0]])
        
    return answer    
