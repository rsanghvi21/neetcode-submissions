class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            key = str(sorted(s))
            if key not in h:
                h[key] = []
            h[key].append(s)
        return list(h.values())

        