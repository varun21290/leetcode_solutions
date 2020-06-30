from collections import defaultdict
class Solution:
    def __init__(self):
        self.result=set()
    
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        class Trie(object):
            def __init__(self):
                self.child = {'#':0}
            def insert(self, word):
                current = self.child
                for l in word:
                    if l not in current:
                        current[l] = {'#':0}
                    current = current[l]
                current['#']=1
            def search(self,word):
                current=self.child
                for l in word:
                    if l in current:
                        current=current[l]
                    elif l not in current:
                        return -1
                if(current['#']==1): return 1
                else: return 0
                
        trie=Trie()
        for word in words:
            trie.insert(word)
            
        def dfs(i,j,graph,c):
            ss=graph[i][j]
            if (ss=='-1'): return
            graph[i][j]='-1'
            c=c+ss
            t=trie.search(c)
#             print(c,t)
            if (t!=-1):
                if t==1: 
                    self.result.add(c)
                dfs(i,j+1,graph,c)
                dfs(i,j-1,graph,c)
                dfs(i+1,j,graph,c)
                dfs(i-1,j,graph,c)
            graph[i][j]=ss
                
                
                

        graph=[['-1']*(len(board[0])+2) for _ in range(len(board)+2)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                graph[i+1][j+1]=board[i][j]
        
        
        for i in range(1,len(graph)-1):
            for j in range(1,len(graph[0])-1):
                dfs(i,j,graph,"")
                
        return list(self.result)
