class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mins, maxs = 1, max(piles)
        res = 0

        while mins <= maxs:
            speed = (maxs + mins) // 2
            time = 0
            for bananas in piles:
                time += math.ceil(float(bananas) / speed)
            if time <= h:
                maxs = speed - 1
                res = speed
            else:
                mins = speed + 1
        return res

