# Leetcode Question 344 (Reversing a String)

def reversestring(self, nums):
  
  def f(left, right):
    
    if (left >= right):
      return s[left],s[right] = s[right], s[left]
      
      f(left+1, right-1)

      f(0,len(s)-1)

# Hence, when the string is being provided as an input, the condition will reverse the given string and provide the output as result.
