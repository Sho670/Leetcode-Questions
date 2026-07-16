# Leetcode Question 134 (Gas Station)

#gas = [1,2,3,4,5]

#cost = [3,4,5,1,2]

#output : 3


class Solution:
  def cancompletecircuit(self, gas: List[int]):
    
    if sum(gas)< sum(cost):
      return -1


    sumgas = 0
    sumcost = 0

    for i in range(len(gas)):
      sumgas += gas[i]
      sumcost += cost[i]

      if sumgas< sumcost:

        index = i+1
        sumgas=0
        sumcost=0

    return index
