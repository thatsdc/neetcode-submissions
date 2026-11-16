class TrieNode: 
    def __init__(self):
        self.childrens = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_trie = self.root
        for c in word: 
            if c not in curr_trie.childrens: 
                curr_trie.childrens[c] = TrieNode()
            curr_trie = curr_trie.childrens[c]

        curr_trie.is_end = True            

    def search(self, word: str) -> bool:
        curr_trie = self.root
        for c in word: 
            curr_trie = curr_trie.childrens.get(c)
            if not curr_trie: return False

        return curr_trie.is_end

    def startsWith(self, prefix: str) -> bool:
        curr_trie = self.root
        for c in prefix: 
            curr_trie = curr_trie.childrens.get(c)
            if not curr_trie: return False

        return True

        
        