#Leetcode Question 33 (Search in Rotated Sorted Array)

# Approach: Binary Search Tree

# The question mostly uses Binary Search Tree Algorithm, only change is we are putting the condition of num[i] being greater than target and nums[mid].
class Solution:
  
  def search():
    
    i=0
    j=len(nums)-1
    
    while i<=j:
      mid = (i+j) // 2
      
      if num [mid]==target:
        return mid
        
      if nums[i]<nums[mid]:
        if nums[i]<=target<nums[mid]:
          j=mid
        
        else:
          i=mid+1
          
      else:
        if nums[mid]<target<=nums[j]:
          i=mid+1
        else:
          j=mid
          
    return -1
          
