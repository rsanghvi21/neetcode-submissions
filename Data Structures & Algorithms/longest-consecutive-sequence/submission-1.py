class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        max = 0
        for n in nums:
            count = 0
            if n - 1 not in s: # start of sequence
                x = n
                while x in s:
                    count += 1
                    x += 1
            if count > max:
                max = count
        return max
        
