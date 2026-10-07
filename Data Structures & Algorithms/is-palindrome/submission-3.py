class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = []
        for c in s:
            if c.isalnum():
                formatted_s.append(c.lower())
        return formatted_s == formatted_s[::-1]