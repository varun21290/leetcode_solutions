class Solution:
    def countBits(self, num: int) -> [int]:
        import math
        l=[0]
        for i in range(1,num+1):
            l.append(1+l[-2**(math.floor(math.log(i,2)))])
        return l
