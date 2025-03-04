class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax,result,l,r = 0,0,0,0,len(height)-1
        while l < r :
            if height[l] <= height[r] :
                if lmax > height[l] :
                    result += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if rmax > height[r] :
                    result += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        return result