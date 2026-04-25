class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxC = 0
        charSet = set[str]()

        l, r = 0, 0

        while r < len(s):
            print(s[r])
            print(charSet)
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            maxC = max(len(charSet), maxC)
            r += 1

        return maxC