class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        graph={}
        vertices=[0]*numCourses
        for edge in prerequisites:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                vertices[edge[0]]=1
                graph[edge[0]]=[edge[1]]

        
        visited=[0]*numCourses
        reVisited=[0]*numCourses
        
        def dfs(key):
            visited[key]=1
            reVisited[key]=1
            if vertices[key]==1:
                for req in graph[key]:
                    if reVisited[req]==1: return False
                    if dfs(req)==False: return False
            reVisited[key]=0
            return True
        
                
        for par in graph.keys():
            if visited[par]==0: flag=dfs(par)
            if flag==False: return False
                
        return True
    
    
    def canFinishBetter(self, numCourses: int, prerequisites: [[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(i, visit, graph):
                return False

        return True

    def dfs(self, i, visit, graph):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True

        visit[i] = -1
        for j in graph[i]:
            if not self.dfs(j, visit, graph):
                return False
        visit[i] = 1

        return True
