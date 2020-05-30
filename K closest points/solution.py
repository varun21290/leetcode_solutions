class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        dist_map={}
        dist_list=[]
        selected=[]
        for point in points:
            dist=point[0]*point[0]+point[1]*point[1]
            dist_list.append(dist)
            if dist in dist_map.keys():
                dist_map[dist].append(point)
            else: dist_map[dist]=[point]
            
        dist_list.sort()
        
        i=0
        while(len(selected)<K):
            selected.extend(dist_map[dist_list[i]])
            i+=1
            
        return selected
            
 # more pythonic way of doing it....
     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def _euclidean(p):
            return math.sqrt(p[0]*p[0] + p[1] * p[1])
        
        return sorted(points, key=_euclidean)[0:K]
