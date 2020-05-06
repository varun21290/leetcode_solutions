def majority(nums,n,e,m,i):
    if(nums.count(nums[n])>e):
        return nums[n]
    else:
        i=i+1
        if (n==0 or n==m-1):
            return 'na'
        if(n<=e):
            o = majority(nums,0+int(m/(2**i)),e,m,i)
            if o!='na' : 
                return o
        if(n>=e):
            o = majority(nums,n+int(m/(2**i)),e,m,i)
            if o!='na' :
                return o
        return 'na'
nums=[1,0,1,1]
n=len(nums)
print (majority(nums,int(n/(2**1)),int(n/2),n,1))     
