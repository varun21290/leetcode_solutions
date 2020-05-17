class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        if(len(s)==0 or len(p)>len(s)): return []
        find=[]
        anagrams={}
        lp=sorted(p)
        len_p=len(p)
        len_s=len(s)
        i=len_p-1
        while(i<len_s):
            if(p.find(s[i])!=-1):
                if (lp==sorted(s[i-len_p+1:i+1])):
                    find.append(i-len_p+1)
                i+=1
            else: i+=len_p
        return find
        
            
    def findAnagrams2(self, s: str, p: str) -> [int]:
        if(len(s)==0 or len(p)>len(s)): return []
        find=[]
        count_p=Counter(p)
        len_p=len(p)
        len_s=len(s)
        i=len_p-1
        while(i<len_s):
            if(p.find(s[i])!=-1):
                if (count_p==Counter(s[i-len_p+1:i+1])):
                    find.append(i-len_p+1)
                i+=1
            else:
                i+=len_p
        return find
            
