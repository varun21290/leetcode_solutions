class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        l=sorted(costs,key=lambda x: x[0]-x[1])
        n=len(costs)
        return (sum(x[0] for x in l[0:n//2]) + sum(x[1] for x in l[n//2:]))
