class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        pre = [0] * len(nums)
        post = [0] * len(nums)

        curr = 1
        for i in range(0, len(nums)):
            pre[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = curr
            output[i] = post[i] * pre[i]
            curr *= nums[i]
        return output