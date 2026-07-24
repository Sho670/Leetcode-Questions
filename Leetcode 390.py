# Leetcode Question 390 (Elimination Game)

class Solution(object):
  def function(self,num):
    head=1
    step=1
    run = nur

    we = True

    while run > 1:
      if we or run %2==1:
        head +=step
      run // = 2
      step *=2
      we = not we
    return head
