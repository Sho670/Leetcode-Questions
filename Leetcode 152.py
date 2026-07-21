# Leetcode Question 152 (Maximum Product Subarray)

class Solution():
  def maximum(self, list-> int):

    highest=1

    lowest=1

    allhigh =1

    allow= 1

    m = max(nums)


for i in nums:
  h =i*allhigh
  l= i*allow
  allhigh = max(h,l,i)
  allow = min(h,l,i)

  if m<ah:
    m = ah
  return m
