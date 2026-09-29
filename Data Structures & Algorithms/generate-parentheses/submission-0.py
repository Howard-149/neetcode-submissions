class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []
        def BT(i,cnt):
            if cnt<0:
                return
            if i==2*n:
                if cnt == 0:
                    ans.append("".join(cur.copy()))
                return
            cur.append("(")
            BT(i+1,cnt+1)
            cur.pop()
            cur.append(")")
            BT(i+1,cnt-1)
            cur.pop()
        BT(0,0)
        return ans
            
