class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        l, r = 0, len(s)
        self.ret = []

        def solveOdd(start):
            tmp = []
            l, r = start - 1, start + 1
            
            while True:
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    return
                
                tmp = s[l:r+1]
                if len(tmp) > len(self.ret):
                    self.ret = list(tmp)
                
                l -= 1
                r += 1

        def solveEven(start):
            tmp = []
            l, r = start, start + 1

            while True:
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    return
                
                tmp = s[l:r+1]
                if len(tmp) > len(self.ret):
                    self.ret = list(tmp)
                
                l -= 1
                r += 1
            
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                solveEven(i)
            if i > 0 and i < len(s) - 1 and s[i - 1] == s[i + 1]:
                solveOdd(i)

        if len(self.ret) == 0:
            return s[0]
        
        return "".join(self.ret)