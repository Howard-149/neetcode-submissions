class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        pieces = []
        def check(s):
            l = 0
            r = len(s)-1
            while l <=r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        def BT(i):
            if i==len(s):
                ans.append(pieces.copy())
                return
            for j in range(i+1,len(s)+1):
                if check(s[i:j]):
                    pieces.append(s[i:j])
                    BT(j)
                    pieces.pop()
        BT(0)
        return ans
            
