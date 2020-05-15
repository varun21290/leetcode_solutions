class Solution:
    def maxSubarraySumCircular(self, arr: [int]) -> int:
        
        new_arr=arr.copy()
        new_arr.sort()
        max_sum=0
        
        if(new_arr[0]==new_arr[-1]):
            if(new_arr[0]>0): return new_arr[0]*len(new_arr)
            else: return new_arr[0]
        
        
        if(new_arr[0]>0):
            for x in new_arr:
                max_sum+=x
            return max_sum
                
        
        def maxSum(A) : 
            n=len(A)//2
#             included=[]
            included_so_far=[]
            max_sum=-30000*30
            max_so_far=0
            i=0
            j=0
#             print (A)
            for i in range(n):
                max_so_far+=A[i]
                
                if(max_so_far>=max_sum): 
                    max_sum=max_so_far
                    start=j
                    end=i
                if(max_so_far<0): 
                    max_so_far=0
                    j=i+1

            
            i=start
            j=start
            max_so_far=0
            while(i<2*n):
                if(i-j==n): 
                    max_so_far=0
                    i=i%n+1
                    j=i
                    continue
                max_so_far+=A[i]
                if(max_so_far>max_sum): 
                    max_sum=max_so_far
                        
                if(max_so_far<0): 
                    max_so_far=0
                    j=i+1
                i+=1
            
            
            return max_sum        
            
        new_arr = arr.copy()
        new_arr.extend(arr)

        return maxSum(new_arr)
