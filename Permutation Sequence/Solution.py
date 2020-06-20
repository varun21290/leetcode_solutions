class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1: return str(n)  
        def factorial(x):
            factorial=1
            for i in range(1,x+1):
                factorial*=i
            return factorial
        
        n_perm=[factorial(i) for i in range(n-1,0,-1)]
        n_list=[_ for _ in range(1,n+1,1)]
        
        perm=''
        i=0
        while (i<n):
            if (k==0):
                for x in range(len(n_list)-1,-1,-1):
                    perm=perm+str(n_list[x])
                break
            else:
                index=k//n_perm[i]+ (1 if k%n_perm[i]>0 else 0)
                perm=perm+str(n_list[index-1])
                n_list.remove(n_list[index-1])
                k=k-(k//n_perm[i])*n_perm[i]
            i+=1
        
        return perm
        
        
