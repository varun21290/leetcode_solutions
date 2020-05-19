class StockSpanner:
    price_history=[]
    price_map=[]
    stack=[]
    def __init__(self):
        self.price_history=[]
        self.price_map=[]
        self.span=[]
        
    def next(self, price: int) -> int:
        j=len(self.price_history)-1
        while(j!=-1 and self.price_history[j]<=price):
            j=self.price_map[j]
        self.price_history.append(price)
        self.price_map.append(j)
        return len(self.price_history)-j-1
    
    def nextBetter(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span)) 
        return span
