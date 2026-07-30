# Leetcode 162 (Find Peak Element)

l=0
j=len(nums)-1

while i<j:
  mid=(i+j)//2
  if nums[mid]<nums[mid+1]:
    i=mid+1
  else:
    j=mid

return j

# Explaination: The solution is highly optimized, using only one while loop for the solution.
