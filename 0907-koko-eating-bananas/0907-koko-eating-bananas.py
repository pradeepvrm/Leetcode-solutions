class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/speed)
            
        #     if totalTime <= h:
        #         return speed
        #     speed += 1
        # return speed

        left = 1
        right = max(piles)

        speed = 0
        while left <= right:
            totalTime = 0
            mid = (left + right) // 2

            for pile in piles:
                totalTime += math.ceil(pile/mid)

            if totalTime <= h:
                speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return speed