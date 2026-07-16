# Leetcode Question 03 (3sum)


class Solution:
  
  def threesum(self, nums: list[int]) -> list[list[int]]:
    nums.sort ()

    answer = []
    for i in range( 0, len(nums)-2)):
      if i>0 and nums[i] ==  nums[i-1]:
        continue



      j = i+1

      k=len(nums)-1
      
