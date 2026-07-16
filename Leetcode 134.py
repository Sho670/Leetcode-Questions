# Leetcode Question 134 (Gas Station)

class Solution:
  def cancompletecircuit(self, gas: List[int]):
    if sum(gas)< sum(cost):
      return -1


    for i in range(len(gas)):
      sumgas += gas[i]
