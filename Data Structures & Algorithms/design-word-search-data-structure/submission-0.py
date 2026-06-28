class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        stack = [(0, self.root)]

        while stack:
            idx, node = stack.pop()

            if idx == len(word):
                if node.word:
                    return True
                continue
            
            c = word[idx]
            if c == '.':
                for child in node.children.values():
                    stack.append((idx + 1, child))
            else:
                if c in node.children:
                    stack.append((idx + 1, node.children[c]))
        return False