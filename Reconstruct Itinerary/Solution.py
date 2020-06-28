import bisect
class Solution:
    def findItinerary(self, tickets: [[str]]) -> [str]:
        graph={}
        itinerary=[]
        
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]]=[ticket[1]]
            else:
                bisect.insort(graph[ticket[0]],ticket[1])
                
        def dfs(graph,itinerary,src):
            if src in graph:
                while(len(graph[src])>0):
                    new_src=graph[src][0]
                    graph[src]=graph[src][1:]
                    dfs(graph,itinerary,new_src)
            itinerary.append(src)
            
            
        dfs(graph,itinerary,"JFK")
        itinerary.reverse()
        return itinerary
        
