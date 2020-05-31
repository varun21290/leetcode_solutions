from collections import deque

class Solution:  
    def minDistance(self, word1: str, word2: str) -> int:
        
        visited = set()
        q = deque([(word1, word2, 0)])
        
        while q:
            w1, w2, dist = q.popleft()
            
            if (w1, w2) not in visited:
                visited.add((w1, w2))

                if w1 == w2:
                    return dist

                while w1 and w2 and w1[0] == w2[0]:
                    w1 = w1[1:]
                    w2 = w2[1:]

                dist += 1
                q.extend([(
                    w1[1:], w2[1:], dist), 
                    (w1, w2[1:], dist), 
                    (w1[1:], w2, dist)])
