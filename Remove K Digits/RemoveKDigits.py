def removeKdigits(self, num: str, k: int)
    new_num=''
    i=len(num)-k
    j=0
    while(i>0):
        minm=j
        while(j<=len(num)-i):
            if(num[j]<num[minm]):minm=j
            j+=1
        new_num = new_num+num[minm]
        i=i-1
        j=minm+1
    return new_num.lstrip('0') or '0'

def removeKdigitsBetter(self, num: str, k: int) -> str:
    new_num=[]
    for n in num:
        while k and new_num and new_num[-1]>n:
            new_num.pop()
            k-=1
        new_num.append(n)
    new_num = new_num[:-k] if k else new_num
    return "".join(new_num).lstrip('0') or "0"
