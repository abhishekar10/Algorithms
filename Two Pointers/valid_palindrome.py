class Solution:
    def isPalindrome(self, s: str) -> bool:
        return ''.join([st for st in s if st.isalnum()])[::-1].lower() == ''.join([st for st in s if st.isalnum()]).lower()