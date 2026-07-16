#Leetcode Question 55 (Jump Game)

class Solution:
  def canjump():
    target = len(nums)-1


    for i in range(len(nums)-2,-1,-1):
      if i+nums[i]>=goal:
        goal=i
    return goal == 0
