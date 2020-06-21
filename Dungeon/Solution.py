class Solution:
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        dp=[[float(inf)]*(len(dungeon[0])+1) for _ in range(len(dungeon)+1)]
        
        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                if(i==len(dungeon)-1 and j==len(dungeon[0])-1):
                    dp[i][j]=abs(dungeon[-1][-1]) if dungeon[-1][-1]<0 else 0
                else: 
                    update=min(dp[i+1][j],dp[i][j+1])
                
                    if(dungeon[i][j]-update>=0): dp[i][j]=0
                    else: dp[i][j] = abs(dungeon[i][j]-update)
                                       
        return dp[0][0]+1
                    
        
