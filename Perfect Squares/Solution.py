import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0,1,2,3]
        
        for i in range(4,n+1):
            dp.append(i)
            
            for x in range(1,int(math.ceil(math.sqrt(i)))+1):
                temp=x*x
                
                if(temp<=i):
                    dp[i]=min(dp[i],1+dp[i-temp])
                else:
                    break
                    
        return dp[n]
        
  ##########################################      
    def numSquaresBetter(self, n: int) -> int:
        while( n % 4 == 0 ):	# Reduction by factor of 4
            n /= 4
			
        if n % 8 == 7:			# If n = 8k + 7, returns 4
            return 4
			
        for a in range( int(sqrt(n))+1 ):	# Check if n = a^2 + b^2, return 0 / 1
            b = int(sqrt(n - a**2))
            if a**2 + b**2 == n:
                return (a>0) + (b>0)
				
        return 3
