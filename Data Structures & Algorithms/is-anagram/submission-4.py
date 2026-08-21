class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s) != len(t):
            return False
        
        for s1, t1 in zip(s, t):
            smap[s1] = smap.get(s1, 0) + 1
            tmap[t1] = tmap.get(t1, 0) + 1

        return smap == tmap



