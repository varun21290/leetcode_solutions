class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = ""
        self.children = []
        self.endOfWord = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self
        for s in word:
            flag=0
            for i in range(len(trie.children)):
                if (trie.children[i].key==s): 
                    trie = trie.children[i] 
                    flag=1
                    break
            if(flag==0):
                new_node = Trie()
                new_node.key=s
                trie.children.append(new_node)
                trie = new_node
        trie.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self
        for s in word:
            flag=0
            for i in range(len(trie.children)):
                if (trie.children[i].key==s): 
                    trie = trie.children[i] 
                    flag=1
                    break
            if (flag==0): return False
        
        return True if trie.endOfWord else False
                
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self
        for s in prefix:
            flag=0
            for i in range(len(trie.children)):
                if (trie.children[i].key==s): 
                    trie = trie.children[i] 
                    flag=1
                    break
            if (flag==0): return False
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
