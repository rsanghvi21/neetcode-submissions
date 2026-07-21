class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        output = []
        for n in nums:
            h[n] = h.get(n, 0) + 1
        i = 0
        while i < k:
            m = max(h, key = h.get)
            output.append(m)
            h[m] = 0
            i = i + 1
        return output 
