# Leetcode Question 18 (Four Sum Problem)

def foursum(self, list-> list[int])

nums.sort()

answer = []
for i in range(0,len(nums)-3):
  if i>0 and nums[i]==nums[i-1]:
    continue


  for l in range(i+1, len(nums)-2):
    if l>i+1 and nums[l]==nums[l-1]:
      continue

  j=i+1
  k=len(nums)-1

  while j<k:
    sum=nums[i]+nums[j]+nums[k]

    if sum==target:
      answer.append([nums[i],nums[j],nums[k])

      j+=1
      k-=1
      
