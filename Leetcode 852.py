# Leetcode Question 852 (Peak index in mountain array)

i=0

j=len(arr)-1

while i<j:
  mid = (i+j) // 2
  
  if arr[mid] < arr[mid+1]:
    i = mid+1
    
  else:
    j = mid

return j

# Returning the increment of mid value with 1, will provide the updated value of i in the if condition.
