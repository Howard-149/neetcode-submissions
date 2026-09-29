class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        used = set()
        def BT():
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for n in nums:
                if n not in used:
                    cur.append(n)
                    used.add(n)
                    BT()
                    cur.pop()
                    used.remove(n)
        BT()
        return ans
