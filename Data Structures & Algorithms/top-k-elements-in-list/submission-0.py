class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        li = []
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        w = list(d.keys())
    
        w.sort(key=lambda x: d[x], reverse=True)
        
        return w[:k]
