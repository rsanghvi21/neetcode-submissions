class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set()
        for n in nums:
            h.add(n)
        
        maxCount = 0
        for n in nums:
            count = 0
            if n-1 in h:
                continue
            count += 1
            x = n + 1
            while x in h:
                count += 1
                x += 1
            maxCount = max(count, maxCount)
        return maxCount
            

            

        