class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        cur = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def BT(i):
            if i==len(digits):
                ans.append("".join(cur.copy()))
                return
            chars = digitToChar.get(digits[i])
            for char in chars:
                cur.append(char)
                BT(i+1)
                cur.pop()
        BT(0)
        return ans