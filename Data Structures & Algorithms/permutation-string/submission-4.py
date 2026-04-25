class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Length = len(s1)
        s1Set = set(s1)
        hashS1 = {}
        hashWindow = {}

        for c in s1:
            hashS1[c] = 1 + hashS1.get(c, 0)

        for c in s2[:s1Length]:
            if c in s1Set:
                hashWindow[c] = 1 + hashWindow.get(c, 0)
        
        if hashS1 == hashWindow:
            return True

        for i in range(s1Length, len(s2)):
            # print(s2[i], s2[i - s1Length])
            if s2[i] in s1Set:
                hashWindow[s2[i]] = 1 + hashWindow.get(s2[i], 0)
            if s2[i - s1Length] in s1Set:
                hashWindow[s2[i - s1Length]] = hashWindow.get(s2[i - s1Length]) - 1

            # print(hashS1, hashWindow)
            if hashS1 == hashWindow:
                return True

        return False