class Solution:
    def intervalIntersection(self, A: [[int]], B: [[int]]) -> [[int]]:
        out=[]
        i=0
        for a in A:
            while(i<len(B)):
                if(B[i][0]>a[1]): break
                if(a[0]>B[i][1]): 
                    i+=1
                    continue
                out.append([max(a[0],B[i][0]),min(a[1],B[i][1])])
                if(B[i][1]>a[1]): 
                    break
                i+=1
        return out
