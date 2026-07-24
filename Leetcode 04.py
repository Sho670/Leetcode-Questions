# Leetcode Question 04 (Four sum)

def foursum(self, nums: list-> list[int]):
  
  nums.sort()

  answer = []

  for i in range(0 len(nums)-3):
    
      if i>0 and nums[i] == nums[i-1]:
          continue

      for l in range(i+1, len(nums)-2):
        
          if l>i+1 and nums[l]==nums[l-1]:
              continue

      j = i+1
    
      k = len(nums)-1

      while j<k:
        sum = nums[i]+nums[j]+nums[k]
        if sum == target:
          answer. append([nums[i],nums[j],nums[k]])
          j+=1
          k-=1
          while j<k and nums[j]==nums[j-1]:
            j+=1
          while j<k and nums[k]==nums[k+1]:
            k-=1

        elif sum>target:
          k-=1
        else:
          j+=1
      return answer

      
  
