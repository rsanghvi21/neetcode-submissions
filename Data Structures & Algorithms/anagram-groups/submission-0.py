class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}
        for s in strs:
            hari = [0,] * 26
            for letters in s:
                index = ord(letters)
                hari[index - 97] += 1
            if tuple(hari) in map:
                map[tuple(hari)].append(s)
            else:
                map[tuple(hari)] = [s]
        return list(map.values())     