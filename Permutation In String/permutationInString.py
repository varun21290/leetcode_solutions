class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)): return False
        count_s1=Counter(s1)
        len_s1=len(s1)
        len_s2=len(s2)
        i=len_s1-1
        while(i<len_s2):
            if(s1.find(s2[i])!=-1):
                if (count_s1==Counter(s2[i-len_s1+1:i+1])):
                    return True
                i+=1
            else:
                i+=len_s1
        return False
    
    def checkInclusionHash(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)): return False
        len_s1=len(s1)
        len_s2=len(s2)
        shashs1=0
        shashs2=0
        
        for i in range(len_s1):
            shashs1=shashs1+hash(s1[i])
            shashs2=shashs2+hash(s2[i])
        if(shashs1==shashs2): return True
        
        for i in range(len_s1,len_s2):
            shashs2=shashs2+hash(s2[i])-hash(s2[i-len_s1])
            if(shashs1==shashs2): return True
        return False
