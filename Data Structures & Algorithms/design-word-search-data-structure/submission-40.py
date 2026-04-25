def convert(letter: str):
    return ord(letter) - 97


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        tmp = self.head
        for i in range(len(word)):
            headAcsii = convert(word[i])
            
            if not tmp.children[headAcsii]:
                tmp.children[headAcsii] = TrieNode()
            tmp = tmp.children[headAcsii]

        tmp.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        def dfs(i, cur):
            if not cur or i == len(word):
                return False
            headAscii = convert(word[i])


            if word[i] == '.':

                for j in range(26):
                    if i == len(word) - 1 and cur.children[j] and cur.children[j].endOfWord:
                        return True

                    ret = dfs(i + 1, cur.children[j])
                    if ret:
                        if word == 'b..':
                            print(ret)
                        return True
                return False
            else:
                if i == len(word) - 1 and cur.children[headAscii] and cur.children[headAscii].endOfWord:
                    return True
                if not cur.children[headAscii]:
                    return False
                
                return dfs(i + 1, cur.children[headAscii])

        return dfs(0, self.head)




