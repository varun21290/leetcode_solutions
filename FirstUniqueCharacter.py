def firstUniqChar(s):
    for i in range(len(s)):
        if s[i]=='1': continue
        if(i==s.rfind(s[i])): return i
        else: s=s.replace(s[i],'1')
    return -1
