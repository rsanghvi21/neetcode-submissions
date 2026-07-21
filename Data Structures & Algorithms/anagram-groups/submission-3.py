class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in h:
                h[key] = []
            h[key].append(word)
            
        return list(h.values())