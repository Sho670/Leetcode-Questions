# Leetcode Question 134 (Gas Station)

#gas = [1,2,3,4,5]

#cost = [3,4,5,1,2]

#output : 3

#Note:  "Greedy Method": Finding optimal solution in that point, can be of lowest or highest at that point.


# In  this question, we are using the first list i.e gas, and visting each of the given numbers, and whenever the sum of gas is more than sum cost, then we will move to the next index with adding index + 1.


class Solution:
  def cancompletecircuit(self, gas: List[int]):
    
    if sum(gas)< sum(cost):
      return -1


    sumgas = 0
    sumcost = 0

    for i in range(len(gas)):
      sumgas += gas[i]
      sumcost += cost[i]

      if sumgas < sumcost:

        index = i+1
        sumgas = 0
        sumcost = 0

    return index
