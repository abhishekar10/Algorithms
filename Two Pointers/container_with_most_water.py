class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        a = 0
        while(l <= r):
            ta = min(height[l],height[r])*(r-l)
            if ta > a:
                a = ta
            if(height[l] < height[r]):
                l+=1
            else:
                r-=1
        return a