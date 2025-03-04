class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,result,c = 0,0,set()
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l+=1
            result = max(result,r-l+1)
            c.add(s[r])
        return result