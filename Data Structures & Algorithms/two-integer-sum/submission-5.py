class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(0, len(nums)):
            n = target - nums[i]
            if n in h:
                return [h[n], i]
            h[nums[i]] = i
        
       