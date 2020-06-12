class RandomizedSet:
    ds={}
    size=0
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds={}
        self.size=0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.ds:
            return False
        else:
            self.ds[val]=val
            self.size+=1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.ds:
            self.ds.pop(val)
            self.size-=1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        sel=random.randint(0,self.size-1)
        return self.ds[list(self.ds.keys())[sel]]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
