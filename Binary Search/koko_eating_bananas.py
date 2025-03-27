class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles_max = max(piles)
        l , r = 1 , piles_max
        n = len(piles)
        res = piles_max
        while l <= r :
            mid = (l + r) //2
            taken = 0
            for i in range (n) :
                taken += math.ceil(piles[i]/mid)
            if taken <= h :
                r = mid - 1
                res = min(res,mid)
            else :
                l = mid + 1
        return res