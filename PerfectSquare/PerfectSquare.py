def isPerfectSquare(self, num: int) -> bool:
    if(num<2): return True
    x=2
    y=num//2
    while(y>=x):
        z=(x+y)//2
        srt=z*z
        if(srt==num): return True
        elif(srt>num): y=z-1
        else: x=z+1
    return False
        
nums = [4,9,144,399]
for x in nums:
    print (x,isPerfectSquare(x))
