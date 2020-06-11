class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x,y=0,len(nums)-1
        i=0
        while(i<=y):
            if(nums[i]==2):  
                nums[i]=nums[y]
                nums[y]=2
                y=y-1
            elif(nums[i]==0):
                nums[i]=nums[x]
                nums[x]=0
                x=x+1
                i=i+1
            else: i=i+1
