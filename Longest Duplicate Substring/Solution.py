class Solution:
    def longestDupSubstring(self, S: str) -> str:
    
        def rabinKarp(pattern, text, p_len, t_len):
  
            hash_map={}
            res=0
            p=0
            t=0
            h=1
            d=26
            q=10000001
        
            for i in range(p_len-1): 
                h = (h*d)%q 
  
            for i in range(p_len): 
                p = (d*p + ord(pattern[i]))%q 
                t = (d*t + ord(text[i+1]))%q
                
            hash_map[p]=0
            
            if(t==p and text[1:p_len+1] == pattern):
                    return pattern,0
            hash_map[t]=1

            for i in range(1,t_len-p_len+1):
                t=(d*(t-ord(text[i])*h) + ord(text[i+p_len]))%q
            
                if t<0: t+=q
                if(t in hash_map and text[i+1:i+1+p_len] == text[hash_map[t]:hash_map[t]+p_len]):
                    return text[i+1:i+1+p_len],hash_map[t]
                else:
                    hash_map[t]=i+1
                
            
            return '',0

        final_res=""
        l=0
        i=0
        r=len(S)-1
        while(l<=r):
            S_len=len(S)
            sub_res=''
            m=(l+r)//2
            pattern=S[i:i+m]
            sub_res,new_i=rabinKarp(pattern,S[i:],m,len(S[i+1:]))
            if sub_res!='': 
                final_res=sub_res
                l=m+1
                S=S[i:]
                i=new_i
            else:
                r=m-1
            
        return final_res
