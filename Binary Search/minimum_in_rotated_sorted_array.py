class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r , res = 0 , len(nums)-1 , float(inf)
        if len(nums) == 1 : return nums[0]
        while l <= r :
            m = (r+l)//2
            res = min(nums[m],res)
            if nums[m] > nums[r] :
                l = m + 1
            else :
                r = m - 1
        return res