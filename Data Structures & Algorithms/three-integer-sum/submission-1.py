class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()

        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sum1 = nums[l] + nums[r] + n
                if sum1 < 0:
                    l += 1
                elif sum1 > 0:
                    r -= 1
                else:
                    res = (n, nums[l], nums[r])
                    s.add(res)
                    r -= 1
                    l += 1
        return [list(res) for res in s]
        