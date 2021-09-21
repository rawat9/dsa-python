class TrieNode:
    def __init__(self):
        self.children = {}

        # terminating is True if node represent the end of the word
        self.terminating = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert the word in the trie
        """
        root = self.root

        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        
        # mark last node as leaf 
        root.terminating = True


    def search(self, word: str) -> bool:
        root = self.root

        for letter in word:
            if letter not in root.children:
                return False
            root = root.children[letter]

        return root.terminating

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for letter in prefix:
            if letter not in root.children:
                return False
            root = root.children[letter]

        return True

    def delete(self, word):
        pass



if __name__ == '__main__':
    strings = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"]
    
    trie = Trie()
    for word in strings:
        trie.insert(word)

    print(trie.search('sell'))  # True
    print(trie.search('best'))  # False
    
    print(trie.startsWith('be'))  # True
    print(trie.startsWith('so'))  # False

