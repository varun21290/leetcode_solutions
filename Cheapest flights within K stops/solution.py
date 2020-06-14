class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        # import collections
        graph=collections.defaultdict(list)
        for u,v,c in flights:
            graph[u].append((v,c))
        queue=collections.deque([(src,0,0)])
        inf=float('inf')
        minCost=inf
        while queue:
            node, steps, costSoFar=queue.popleft()
            
            if(node==dst):
                minCost=min(minCost,costSoFar)
                continue
                
            if(steps>K or costSoFar>minCost):
                continue
                
            for v,c in graph[node]:
                queue.append((v,steps+1,costSoFar+c))
        
        return minCost if minCost!=inf else -1
