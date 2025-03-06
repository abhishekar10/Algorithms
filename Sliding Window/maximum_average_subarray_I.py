class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = current_sum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum / k