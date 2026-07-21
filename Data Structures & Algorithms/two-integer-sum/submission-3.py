class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in h:
                x = h.get(diff)
                return [x, i]
            h[nums[i]] = i    