class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCount = 0
        for n in s:
            count = 0
            # Check if n has a left neighbor
            if n - 1 in s:
                continue
            # Right neighbors
            count += 1
            x = n + 1
            while x in s:
                count += 1
                x += 1
            if count >= maxCount:
                maxCount = count
        return maxCount
