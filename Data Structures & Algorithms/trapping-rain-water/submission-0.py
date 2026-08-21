class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minArr = [0] * len(height)

        maxL = 0
        for i in range(len(height)):
            if height[i] > maxL:
                maxL = height[i]
            maxLeft[i] = maxL

        maxR = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > maxR:
                maxR = height[i]
            maxRight[i] = maxR

        for i in range(len(height)):
            minArr[i] = min(maxLeft[i], maxRight[i])

        water = 0
        for i in range(len(height)):
            if minArr[i] - height[i] > 0:
                water += minArr[i] - height[i]
        return water