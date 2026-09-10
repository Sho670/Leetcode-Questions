#Leetcode Question 128 (Longest Consecutive Sequence)

def longestconsecutive(self, List->[nums][int][int]):
    
    if len(nums)==0:
      return 0
        
    s=set(nums)
    
    m=1
    
    for i in s:
        if i-1 not in s:
            c=1
            
            while i+1 in s:
                c+=1
                i+=1
                
            if m<c:
                m=c
                
    return m
