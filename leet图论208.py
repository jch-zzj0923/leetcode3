class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end = False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self, word: str) -> None:
        cur=self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
        cur.is_end=True
    def search(self, word: str) -> bool:
        cur=self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur=cur.children[ch]
        return cur.is_end
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur=cur.children[ch]
        return True
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # returns True
    print(trie.search("app"))     # returns False
    print(trie.startsWith("app")) # returns True
    trie.insert("app")
    print(trie.search("app"))    