def singleNonDuplicate(self, nums: [int]) -> int:
    if(len(nums)==1): return nums[0]
    def check(nums,x,y):
        m=(x+y)//2
        if(m==0): return nums[m]
        if(m==len(nums)-1): return nums[m]
        if(nums[m-1]!=nums[m] and nums[m+1]!=nums[m]): 
            return nums[m]
        elif (nums[m-1]==nums[m] and m%2==0):
            return check(nums,x,m)
        elif (nums[m+1]==nums[m] and m%2==0):
            return check(nums,m,y)
        elif (nums[m-1]==nums[m] and m%2!=0):
            return check(nums,m+1,y)
        elif (nums[m+1]==nums[m] and m%2!=0):
            return check(nums,x,m-1)

        return check(nums,0,len(nums)-1)
