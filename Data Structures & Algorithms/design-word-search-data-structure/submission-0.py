class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}   
            cur = cur[char]
        cur['End'] = {}

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for child in cur.keys():
                        if dfs(i+1,cur[child]):
                            return True
                    return False
                else:
                    if word[i] not in cur:
                        return False
                    else:
                       cur = cur[word[i]]
            return "End" in cur
        return dfs(0,self.trie)