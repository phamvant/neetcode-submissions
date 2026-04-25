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

        for i in range(len(word)):
            headAcsii = convert(word[i])
            
            if not tmp.children[headAcsii]:
                tmp.children[headAcsii] = TrieNode()
            tmp = tmp.children[headAcsii]

        tmp.endOfWord = True


    def search(self, word: str) -> bool:
        tmp = self.head

        for i in range(len(word)):
            headAscii = convert(word[i])

            if not tmp.children[headAscii]:
                return False
            
            tmp = tmp.children[headAscii]

        if not tmp.endOfWord:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        tmp = self.head

        for i in range(len(prefix)):
            headAscii = convert(prefix[i])

            if not tmp.children[headAscii]:
                return False
            
            tmp = tmp.children[headAscii]
        
        return True
        