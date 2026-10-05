class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def s_to_i(s:str):
            number = 0
            d = {
                "0":0,
                "1":1,
                "2":2,
                "3":3,
                "4":4,
                "5":5,
                "6":6,
                "7":7,
                "8":8,
                "9":9
            }
            for i in range(len(s)):
                number = number*10 + d[s[i]]
            return number
        return str(s_to_i(num1) * s_to_i(num2))