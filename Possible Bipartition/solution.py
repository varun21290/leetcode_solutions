class Solution:
    def possibleBipartition(self, N: int, dislikes: [[int]]) -> bool:
        matrix=[[0]*N for _ in range(N)]
        for dislike in dislikes:
            matrix[dislike[0]-1][dislike[1]-1]=1
            matrix[dislike[1]-1][dislike[0]-1]=1
        queue=[0]
        color={}
        color[0]=1
        n=0
        while len(queue)>0:
            for i in range(len(matrix[0])):
                if matrix[queue[0]][i]==1:
                    if i not in color:
                        color[i]= 1 if color[queue[0]]==0 else 0
                        queue.append(i)
                    elif color[i]==color[queue[0]]:
                        return False
            queue=queue[1:]
            n+=1
            if(len(queue)==0 and n<N):
                queue.append(n)
                if (n not in color):
                    color[n]=1
        return True
                    
