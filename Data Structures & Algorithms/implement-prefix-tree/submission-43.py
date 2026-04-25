import string

def convert(letter: str):
    return ord(letter) - 97

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        tmp = self.head
        for char in word:
            idx = convert(char)
            if not tmp.children[idx]:
                tmp.children[idx] = TrieNode()
            # Move to the child node first
            tmp = tmp.children[idx]
        # Mark the last node as the end of a word
        tmp.endOfWord = True

    def search(self, word: str) -> bool:
        tmp = self.head
        for char in word:
            idx = convert(char)
            if not tmp.children[idx]:
                return False
            tmp = tmp.children[idx]
        # Return True only if the path exists AND it's a complete word
        return tmp.endOfWord

    def startsWith(self, prefix: str) -> bool:
        tmp = self.head
        for char in prefix:
            idx = convert(char)
            if not tmp.children[idx]:
                return False
            # CRITICAL: You must move the pointer to the next node!
            tmp = tmp.children[idx]
        return True