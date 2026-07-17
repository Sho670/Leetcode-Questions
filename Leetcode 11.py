# Leetcode Question 11 (Container with most water)


class Solution:
  
  def function():

    minarea = 0
    l =0
    r len(height) -1

    while l<r:
      if height[l]<= height[r]:
        h = height[r]

      else:
        h = height[r]

      w = r-l

      area = h * w
      minarea = max(minarea, area)

      if height [i]<= height[r]:
        l +=1
      else:
        r = -1

  return minarea
  

    

  
