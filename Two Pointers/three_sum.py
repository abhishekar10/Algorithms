class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                tempsum = nums[i]+nums[l]+nums[r]
                if tempsum == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif tempsum > 0:
                    r-=1
                else:
                    l+=1
        return result                                 