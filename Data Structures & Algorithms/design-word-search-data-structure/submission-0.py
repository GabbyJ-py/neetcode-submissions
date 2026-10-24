class WordDictionary:

    def __init__(self):
        self.trie = {}        

    def addWord(self, word: str) -> None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        d["*"] = "*"        

    def search(self, word: str) -> bool:
        def dfs(d, i):
            if i == len(word):
                return "*" in d

            char = word[i]

            if char != ".":
                if char not in d:
                    return False
                return dfs(d[char], i+1)

            for child in d:
                if child != "*":
                    if dfs(d[child], i+1):
                        return True
            return False

        return dfs(self.trie, 0)


        
