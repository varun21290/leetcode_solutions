class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        arr=[]
        for i in range(len(string)):
            if(string[i] in freq.keys()): freq[string[i]]=freq[string[i]]+1
            else: freq[string[i]]=1
        
        
        for key,item in freq.items():
            arr.append([key,item])
    
        from operator import itemgetter
        res = sorted(arr, key = itemgetter(1))
        s=''
        for i in range(len(res),0,-1):
            l=[res[i-1][0]]*res[i-1][1]
            for x in l:
                s=s+x
        return s
