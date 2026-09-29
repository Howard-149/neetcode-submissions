class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
                cur = cur[char]
            else:
                cur = cur[char]
        cur['End'] = {}

    def search(self, word: str) -> bool:
        cur = self.trie
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return 'End' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
        