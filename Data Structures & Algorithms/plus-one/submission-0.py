class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            d = digits[i]
            ans.append((d+carry)%10)
            carry = (d+carry)//10
        if carry:
            ans.append(carry)
        return ans[::-1]
