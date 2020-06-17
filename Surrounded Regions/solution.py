class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        if row==0: return
        col=len(board[0])
                    
        for i in range(row):
            for j in range(col):
                
                if board[i][j]=='O': board[i][j]='-'
            
        def floodFill(a,b):    
            board[a][b]='O'
            l,r,u,d=b-1,b+1,a-1,a+1
            if l>=0 and board[a][l]=='-': floodFill(a,l)
                
            if r<col and board[a][r]=='-': floodFill(a,r)
                
            if u>=0 and board[u][b]=='-': floodFill(u,b)
                
            if d<row and board[d][b]=='-': floodFill(d,b)
            
        for i in [0,row-1]:
             for j in range(col):
                if board[i][j]=='-': floodFill(i,j)           
                
        for i in range(1,row-1):
            for j in [0,col-1]:  
                
                if board[i][j]=='-': floodFill(i,j)
                    
        
        for i in range(row):
            for j in range(col):           
                if board[i][j]=='-': board[i][j]='X'
