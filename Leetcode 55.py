#Leetcode Question 55 (Jump Game)

# Approach  Used : Greddy Approach

# Time Complexity: O(n), because the code is able to complete the execution  in only one for loop

class Solution:
  def canjump():
    target = len(nums)-1


    for i in range(len(nums)-2,-1,-1):
      if i+nums[i] >= target:
        target =i
    return target == 0
