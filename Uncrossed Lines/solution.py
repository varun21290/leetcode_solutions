class Solution:
    def maxUncrossedLines(self, A: [int], B: [int]) -> int:
#         dp=[0]*(len(A)+1)
#         for i in range((len(A)+1)):
#             dp[i]=[0]*(len(B)+1)

        elem = set(A)&set(B)
        A,B = [a for a in A if a in elem],[b for b in B if b in elem]
        dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
        i=len(A)-1
        while(i>=0):
            j=len(B)-1
            while(j>=0):
                if(A[i]==B[j]):
                    dp[i][j]=1+dp[i+1][j+1]
                if(A[i]!=B[j]):
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
                j-=1
            i-=1
        return dp[0][0]
