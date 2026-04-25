class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in range(len(strs)):
            tmp = [0] * 26
            for j in range(len(strs[i])):
                tmp[ord(strs[i][j]) - ord('a')] += 1
            if tuple(tmp) not in hashMap:
                hashMap[tuple(tmp)] = []
            hashMap[tuple(tmp)].append(strs[i])
        return list(hashMap.values())
