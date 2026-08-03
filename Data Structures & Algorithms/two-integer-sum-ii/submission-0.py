class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        left, right = 0, 0

        #while (r > 0 and numbers[r] > target):
        #    r -= 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                left = l + 1
                right = r + 1
                break
        return [left, right]


        