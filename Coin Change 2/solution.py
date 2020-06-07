class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        if amount==0: return 1
        dp=[]
        for _ in range(len(coins)+1):
            l=[1]
            l.extend([0]*amount)
            dp.append(l)
        dp[0][0]=0
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                dp[i][j]=dp[i-1][j]+ (0 if j<coins[i-1] else dp[i][j-coins[i-1]])
        return dp[-1][-1]
    
    
    def changeBetter(self, amount: int, coins: [int]) -> int:
        changes = [0] * (amount + 1)
        changes[0] = 1 
        for coin in coins:
            for i in range(0, amount - coin + 1):
                if changes[i]:
                    changes[i + coin] += changes[i]
        return changes[amount]
        
