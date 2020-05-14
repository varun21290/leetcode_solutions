class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data={}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t=self.data
        for s in word:
            if (s not in t): t[s] = {}
            t=t[s]
        t['-'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.data
        for s in word:
            if (s not in t): return False
            t=t[s] 

        return True if '-' in t else False
                
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t=self.data
        for s in prefix:
            if(s not in t): return False 
            t=t[s]
        return True
#         return False if trie.endOfWord else True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
