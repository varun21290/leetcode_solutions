class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        max_length=0
        length_map={}
        zero=0
        one=0
        
        for i in range(len(nums)):
            if(nums[i]==0): zero+=1
            else: one+=1
            diff=zero-one
            if(diff==0):
                max_length=i+1
            
            if(diff in length_map):
                if(max_length < i-length_map[diff]):
                    max_length = i-length_map[diff]
            else:
                length_map[diff] = i
        return max_length
